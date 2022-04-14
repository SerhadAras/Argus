const fs = require("fs");
const https = require("https");
const process = require("process");
const express = require("express");
const LogFile = require("logfile");

// Create express Router
const router = express.Router();

module.exports = {
    router: router,
    start: (serviceName, path, clientAuth = true) => {
        const logFile = LogFile.createLogFile(serviceName);
        const logger = logFile.getLogger();

        // Create Webserver
        const app = express();

        // Register logging middleware
        app.use(logFile.createMiddleware());

        app.use((req, res, next) => {

            if( clientAuth && !req.client.authorized && req.headers["ssl-client-verify"] !== "SUCCESS" )
            {
                res.status(401).send({
                    status: 401,
                    msg: "Unauthorized, invalid client certificate.",
                    reason: req.client.authorizationError
                });
                return;
            }

            next();
        });

        // Register body parser middleware
        app.use(express.json());

        // Use router
        app.use(path, router);

        // Register 404 route
        app.all("*", async (req, res) => {
            res.status(404).send({status: 404, message: "This route does not exist!"});
        });

        if(clientAuth)
        {
            return https.createServer({

                cert: fs.readFileSync(process.env.CERT_PATH || "cert.crt"),
                key: fs.readFileSync(process.env.KEY_PATH || "cert.key"),

                ca: fs.readFileSync(process.env.CA_PATH || "ca.crt"),
                requestCert: clientAuth,
                rejectUnauthorized: false

            }, app).listen(process.env.PORT || 3000, () => {
                logger.info(`Server started on port ${process.env.PORT || 3000}.`);
            });
        }
        else
        {
            return app.listen(process.env.PORT || 3000, () => {
                logger.info(`Server started on port ${process.env.PORT || 3000}.`);
            });
        }
    }
};
