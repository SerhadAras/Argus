const { v4: uuid } = require("uuid");
const createService = require("service");

const service = createService("gateway", "/api/v1/checks");
const { redis, router } = service;

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
            promises.push(redis.insert("jobs:" + checklist, job));
        }
    }

    await Promise.all(promises);
    res.status(201).send({status: 201, message: "Checks have succesfully been requested", tracker: request.tracker});
});

router.get("/poll", async (req, res) => {
    const results = await redis.popEmpty("results");
    if(!results)
    {
        res.status(200).contentType("application/json").send([]);
        return;
    }

    res.status(200).contentType("application/json").send(results.map(x => JSON.parse(x)));
});

router.get("/checklists", async (req, res) => {
    const results = await redis.sortedGet("checklists");
    var checks = [];

    results.forEach(x => {
        var index = results.indexOf(x);

        if(index % 2 === 0)
        {
            if(results[index + 1] > Date.now())  //only select the checks that are not expired
            {
                checks.push(x);
            }
        }

    });

    res.status(200).contentType("application/json").send(checks);
});

service.start();
