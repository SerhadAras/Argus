const { v4: uuid } = require("uuid");
const createService = require("service");

const service = createService("gateway", "/api/v1/checks");
const { redis, router } = service;

router.post("/request", async (req, res) => {

    const request = req.body;
    const availableChecklists = await getChecklists();

    // Add a tracker to the the request
    if(!("tracker" in request))
    {
        request.tracker = uuid();
    }

    // Build checklists set
    const checklists = new Set();

    if("tags" in request)
    {
        for(const tag of request.tags)
        {
            const checkl = availableChecklists.filter( x => {
                return x.tags.includes(tag);
            });
            checkl.forEach(x => checklists.add(x));
        }
    }

    if("checklists" in request)
    {
        const checkl = availableChecklists.filter( x => {
            return request.checklists.includes(x.name);
        });
        checkl.forEach(x => checklists.add(x));
    }

    // Build target set
    const targets = new Set();
    const availableTypes = new Set(availableChecklists.flatMap(x => x.type));

    for(const type of availableTypes)
    {
        if(type in request.targets)
        {
            request.targets[type].forEach(x => {
                targets.add({
                    target: x,
                    type: type
                });
            });
        }
    }

    const promises = [];

    for(const target of targets)
    {
        for(const checklist of checklists)
        {
            if(!checklist.type.includes(target.type))
            {
                // Do not enqueue jobs that do not produce results
                continue;
            }

            // Enqueue job
            const job = {
                id: checklist.name,
                tracker: request.tracker,
                target: target.target,
                type: target.type
            };

            promises.push(redis.insert("jobs:" + checklist.name, job));
        }
    }

    if(promises.length === 0)
    {
        res.status(400).send({
            status: 400,
            message: "No checklists could be requested, malformed request.",
            requested: promises.length
        });
        return;
    }

    // Wait until everything is enqueued.
    await Promise.all(promises);

    // Send response
    res.status(201).send({
        status: 201,
        message: "Checklists have succesfully been requested.",
        tracker: request.tracker,
        requested: promises.length
    });
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
    res.status(200).contentType("application/json").send(await getChecklists());
});

/**
     * @param {string} key the queue in which the value will be stored
     * @param {any} value
     * @returns {Promise<any>}
     * performs a sorted set on a certain queue
     */

/**
 * @returns {Array} array with all checklists and its flags
 */
async function getChecklists()
{
    const results = await redis.sortedGet("checklists");
    var checks = [];

    results.forEach(x => {
        var index = results.indexOf(x);

        if(index % 2 === 0)
        {
            if(parseInt(results[index + 1]) > Date.now())  //only select the checks that are not expired
            {
                checks.push(JSON.parse(x));
            }
        }

    });

    return checks;
}

service.start( (process.env.TLS_ENABLED || "TRUE").toLowerCase() === "true");
