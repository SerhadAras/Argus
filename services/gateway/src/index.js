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

    const checklists = new Set();
    const availableChecklists = await getChecklists();

    if("tags" in request)
    {
        for(const tag of request.tags)
        {
            const checkl = availableChecklists.filter( x => {
                return x.tags.includes(tag);
            });
            checkl.forEach(x => checklists.add(x.name));
        }
    }
    if("checklists" in request)
    {
        const checkl = availableChecklists.filter( x => {
            return request.checklists.includes(x.name);
        });
        checkl.forEach(x => checklists.add(x.name));
    }

    const promises = [];

    for(const domain of request.domains)
    {
        for(const checklist of checklists)
        {
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
            if(results[index + 1] > Date.now())  //only select the checks that are not expired
            {
                checks.push(JSON.parse(x));
            }
        }

    });

    return checks;
}

service.start( (process.env.TLS_ENABLED || "TRUE").toLowerCase() === "true");
