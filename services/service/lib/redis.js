const process = require("process");
const LogFile = require("logfile");
const RedisClient = require("redis");

module.exports = (serviceName) => {
    const logFile = LogFile.createLogFile(serviceName);
    const logger = logFile.getLogger();

    // Create redis client
    const redisClient = new RedisClient(process.env.REDIS_HOST || "localhost",
        process.env.REDIS_PORT || 26379, process.env.REDIS_PASSWORD || "");

    // Register redis events
    redisClient.onError((err) => {
        logger.error(err.message);
    });

    redisClient.onConnect(() => {
        logger.debug("Connecting to the redis database.");
    });

    redisClient.onReconnect(() => {
        logger.debug("Reconnecting to the redis database.");
    });

    redisClient.onReady(() => {
        logger.info("Connected to the redis database.");
    });

    redisClient.onDisconnect(() => {
        logger.info("Disconnected from the redis database.");
    });

    // Connect to the redis client
    logger.debug(`Connecting to the redis database at ${process.env.REDIS_HOST ||
        "localhost"}:${process.env.REDIS_PORT || 26379}`);

    return redisClient;
};
