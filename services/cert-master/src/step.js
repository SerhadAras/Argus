const fs = require("fs");
const util = require("util");
const exec = util.promisify(require("child_process").exec);
const temp = require("temp");

temp.track();

/**
 * A wrapper around the step-cli.
 */
class StepProvisioner
{
    /**
     * constructor.
     *
     * @param {string} root The path to the root certificate.
     * @param {string} caUrl The url to connect to the CA.
     * @param {any} logger A logger object.
     * @param {string} stepCli The path to the step-cli executable.
     */
    constructor(root, caUrl, logger, stepCli = "step")
    {
        this.root = root;
        this.caUrl = caUrl;
        this.logger = logger;
        this.stepCli = stepCli;
    }

    /**
     * Get a temporary file.
     *
     * @param {} contents
     */
    async getTempFile(contents = null)
    {
        return new Promise((resolve, reject) => {
            temp.open("step", (err, result) => {
                if(err)
                {
                    reject(err);

                    return;
                }

                if(contents)
                {
                    fs.writeFileSync(result.path, contents);
                }

                resolve(result.path);
            });
        });
    }

    /**
     * Get the serial number of a specific certificate.
     *
     * @param {string} cert The certificate in string format.
     */
    async getSerialNumber(cert)
    {
        const crtFile = await this.getTempFile(cert);

        const { stdout } = await exec(`${this.stepCli} certificate inspect "${crtFile}" --format json`);
        const certInfo = JSON.parse(stdout);

        // Clean up temporary
        temp.cleanupSync();

        return certInfo.serial_number;
    }

    /**
     * Renew a certificate.
     *
     * @param {string} crt The certificate in string format.
     * @param {string} key The key of the certificate in string format.
     */
    renew(crt, key)
    {
        return new Promise(async (resolve, reject) => {

            // Get temp files
            const crtFile = await this.getTempFile(crt);
            const keyFile = await this.getTempFile(key);
            const newFile = await this.getTempFile();

            // Renew certificate
            //   step ca renew -f --root=root.crt --ca-url=CA:443 cert.crt cert.key --out newCert.crt
            exec(`${this.stepCli} ca renew -f --root="${this.root}" ` +
                `--ca-url="${this.caUrl}" "${crtFile}" "${keyFile}" --out "${newFile}"`)
                .catch(e => {

                    this.logger.error("Failed renewing certificate", e);
                    reject();
                }).then(() => {
                    resolve(fs.readFileSync(newFile));
                }).finally(() => temp.cleanupSync());
        });
    }
}

module.exports = StepProvisioner;
