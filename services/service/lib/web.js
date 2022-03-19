const process = require("process");
const express = require("express");
const LogFile = require("logfile");

// Create express Router
const router = express.Router();

module.exports = {
    router: router,
    start: (serviceName, path) => {
        const logFile = LogFile.createLogFile(serviceName);
        const logger = logFile.getLogger();

        // Create Webserver
        const app = express();

        // Register logging middleware
        app.use(logFile.createMiddleware());

        // Register body parser middleware
        app.use(express.json());

        // Use router
        app.use(path, router);

        // Register 404 route
        app.all("*", async (req, res) => {
            res.status(404).send({status: 404, message: "This route does not exist!"});
        });

        return app.listen(process.env.PORT || 3000, () => {
            logger.info(`Server started on port ${process.env.PORT || 3000}.`);
        });
    }
};
