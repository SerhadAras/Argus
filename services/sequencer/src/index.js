const createService = require("service");

const service = createService("sequencer", "/api/v1");
const { logger, redis, router } = service;

// Get job from specified queue
router.get("/job/:id", async (req, res) => {

    const queueId = req.params.id;
    logger.debug(`Finding jobs in ${queueId} queue.`);

    const job = await redis.pop("jobs:" + queueId);

    if(!job || job === "")
    {
        res.status(404).send({status: 404, message: "No jobs are ready for execution"});
        return;
    }

    res.status(200).contentType("application/json").send(job);
});

router.post("/jobs", async (req, res) => {

    const queueId = req.body.resource.metadata.labels.checklist;
    const len = await redis.length("jobs:" + queueId);

    res.status(200).contentType("application/json").send(len.toString());
});

// Post results
router.post("/results", async (req, res) => {

    const results = req.body;

    await redis.insert("results", results);

    res.status(201).send({status: 201, message: "Results successfully registered."});
});

service.start();
