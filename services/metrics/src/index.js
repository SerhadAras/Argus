const createService = require("service");

const service = createService("metrics", "/api/v1");
const { redis, router } = service;

// Get metrics for a resource
router.post("/jobs", async (req, res) => {

    const queueId = req.body.resource.metadata.labels.checklist;
    const len = await redis.length("jobs:" + queueId);

    res.status(200).contentType("application/json").send(len.toString());
});

service.start( false );
