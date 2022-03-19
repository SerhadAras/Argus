const process = require("process");
const LogFile = require("logfile");
const createRedis = require("./redis.js");
const app = require("./web.js");

module.exports = (serviceName, path = "") => {

    // Create logger
    const logFile = LogFile.createLogFile(serviceName, process.env.LOGLEVEL || "http");
    const logger = logFile.getLogger();

    // Create Redis client
    const redis = createRedis(serviceName);

    let server;

    /**
     * Graceful Shutdown
     */
    async function shutdown()
    {
        logger.info("Shutting down " + serviceName + ".");

        redis.disconnect();

        if(server)
        {
            server.close(() => {
                logger.info("Closed Web Server.");
            });
        }
    }

    // Catch SIGINT and SIGTERM
    process.on("SIGINT", shutdown)
        .on("SIGTERM", shutdown);

    // Return essential service objects
    return {
        logger: logger,
        redis: redis,
        router: app.router,
        start: () => server = app.start(serviceName, path),
        shutdown: shutdown
    };
};
