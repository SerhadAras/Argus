const process = require("process");
const axios = require("axios");

const createService = require("service");

const service = createService("metrics", "/api/v1", {
    redis: {
        enabled: true,
        sentinel: false
    }
});
const { redis, router } = service;

// Get metrics for a resource
router.post("/metric", async (req, res) => {

    const app = req.body.resource.metadata.labels.app.toLowerCase().trim();
    if(app === "checklist")
    {
        const queueId = req.body.resource.metadata.labels.checklist;
        const len = await redis.length("jobs:" + queueId);

        res.status(200).contentType("application/json").send(len.toString());
    }
    else if(app === "selenium-node-chrome")
    {
        const SELENIUM_URL = process.env.SELENIUM_URL || "http://selenium-hub:4444";

        const queueSize = (await axios.post(SELENIUM_URL + "/graphql", {
            query: "query Summary { grid { sessionQueueSize  }}"
        })).data.data.grid.sessionQueueSize;


        res.status(200).contentType("application/json").send(queueSize.toString());
    }
    else
    {
        res.status(404).contentType("application/json").send("0");
    }
});

service.start( false );
