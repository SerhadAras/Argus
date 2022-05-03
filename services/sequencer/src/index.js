const process = require("process");
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
        res.status(404).send({status: 404, message: "No jobs are ready for execution."});
        return;
    }

    res.status(200).contentType("application/json").send(job);
});

// Post results
router.post("/results", async (req, res) => {

    const results = req.body;

    await redis.insert("results", results);

    res.status(201).send({status: 201, message: "Results successfully registered."});
});

router.post("/pushback", async (req, res) => {

    await redis.insertFront("jobs:" + req.body.id, req.body.domain);

    res.status(201).send({status: 201, message: "Job succesfully inserted."});
});

router.post("/advertise", async (req, res) => {

    await redis.sortedSet("checklists", req.body);

    res.status(201).send({status: 201, message: "Checklist advertised."});
});

service.start( (process.env.TLS_ENABLED || "TRUE").toLowerCase() === "true");
