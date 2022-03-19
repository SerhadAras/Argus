var redis = require("ioredis"),
    client = redis.createClient();

client.on("error", function (err) {
    console.log("Error " + err);
});


client.zadd("myzset", Date.now(), "dns");
client.zadd("myzset", Date.now(), "ip");
client.zadd("myzset", Date.now(), "geoip");

client.zrevrange("myzset", 0, -1, function (err, list) {
    if (err)
    {
        throw err;
    }
    console.log("plain range:", list);
});

client.zrevrange("myzset", 0, -1, "withscores", function (err, listwithscores) {
    if (err)
    {
        throw err;
    }
    console.log("with scores:", listwithscores);
});

client.quit(function (err, res) {
    if (err)
    {
        throw err;
    }
    console.log("Exiting from quit command.");
    res.status(200);
});
