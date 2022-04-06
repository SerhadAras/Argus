const fs = require("fs");
const process = require("process");

const k8s = require("@kubernetes/client-node");

// Load k8s api client
const kc = new k8s.KubeConfig();
kc.loadFromDefault();
const k8sApi = kc.makeApiClient(k8s.CoreV1Api);

// Refresh CA secret
module.exports = async () => {

    const namespace = process.env.NAMESPACE || "default";
    const name = "autocert-ca-certificate";

    const list = await k8sApi.listNamespacedSecret(namespace);

    if(list.body.items.map(x => x.metadata.name).includes(name))
    {
        await patch(name, namespace);
    }
    else
    {
        await create(name, namespace);
    }
};

/**
 * Create a new Certificate Authority Secret.
 * @param {string} name The name of the secret.
 * @param {string} namespace The namespace the secret lives in.
 */
async function create(name, namespace)
{
    k8sApi.createNamespacedSecret(namespace, {
        metadata: {
            name: name,
            namespace: namespace
        },
        data: {
            "ca.crt": fs.readFileSync(process.env.CA_PATH).toString("base64")
        }
    });
}

/**
 * Patch a Certificate Authority Secret with a new certificate.
 * @param {string} name The name of the secret.
 * @param {string} namespace The namespace the secret lives in.
 */
async function patch(name, namespace)
{
    k8sApi.replaceNamespacedSecret(name, namespace, {
        metadata: {
            name: name,
            namespace: namespace
        },
        data: {
            "ca.crt": fs.readFileSync(process.env.CA_PATH).toString("base64")
        }
    });
}
