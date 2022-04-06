const express = require("express");
const process = require("process");
const createService = require("service");
const StepProvisioner = require("./step.js");
const refreshCA = require("./ca-secret.js");

const service = createService("cert-master", "/api/v1/certificate", { redis: { enabled: false } });
const { logger, router } = service;

const step = new StepProvisioner(process.env.CA_PATH || "ca.crt", process.env.CA_URL || ":443",
    logger, process.env.STEP_CLI || "step");

router.use(express.text());

router.post("/renew", async (req, res) => {
    const crtkey = req.body;

    const crt = crtkey.substr(0, /-*BEGIN.*KEY-*/g.exec(crtkey).index).trim();
    const key = crtkey.substr(/-*BEGIN.*KEY-*/g.exec(crtkey).index).trim();

    const serial = await step.getSerialNumber(crt);

    step.renew(crt, key).then(newCert => {
        logger.info(`Renewed ${serial}.`);
        res.contentType("text/plain").send(newCert);
    }).catch(e => {
        logger.warn(`Failed renewing ${serial}.`, e);

        res.status(500).send({
            status: 500,
            msg: "Failed renewing certificate, check logs for more info."
        });
    });
});

// Start refresh
const interval = setInterval(async () => {
    refreshCA().then(() => {
        logger.info("Refreshed CA secret.");
    }).catch((e) => {
        logger.error("Failed refreshing CA secret.", e);
    });
}, 5 * 24 * 60 * 60 * 1000);

refreshCA().then(() => {
    logger.info("Refreshed CA secret.");
}).catch((e) => {
    logger.error("Failed refreshing CA secret.", e);
});

process.on("SIGINT", () => clearInterval(interval));
process.on("SIGTERM", () => clearInterval(interval));

service.start();
