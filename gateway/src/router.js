const process = require("process");
const express = require("express");
const LogFile = require("logfile");
const RedisClient = require("redis");
const { v4: uuid } = require("uuid");

// Get the logger instance
const logFile = LogFile.createLogFile("gateway");
const logger = logFile.getLogger();

// Create redis client
const redisClient = new RedisClient(process.env.REDIS_HOST || "localhost", process.env.REDIS_PORT || 26379);

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

// Create an express router
const router = express.Router();

router.post("/request", async (req, res) => {

    const request = req.body;

    if(!("tracker" in request))
    {
        request.tracker = uuid();
    }

    const promises = [];

    for(const i in request.domains)
    {
        const domain = request.domains[i];

        for(const j in request.checklists)
        {
            const checklist = request.checklists[j];
            const job = {
                id: checklist,
                tracker: request.tracker,
                domain: domain
            };
            promises.push(redisClient.insert("jobs:" + checklist, job));
        }
    }

    await Promise.all(promises);
    res.status(201).send({status: 201, message: "Checks have succesfully been requested", tracker: request.tracker});
});

router.get("/poll", async (req, res) => {
    const results = await redisClient.popEmpty("results");
    if(!results)
    {
        res.status(200).contentType("application/json").send([]);
        return;
    }

    res.status(200).contentType("application/json").send(results.map(x => JSON.parse(x)));
});

router.get("/checklists", async (req, res) => {
    res.status(501).send();
});

// Create graceful shutdown method
router.close = async () => {
    await redisClient.disconnect();
};

// Export the router
module.exports = router;
