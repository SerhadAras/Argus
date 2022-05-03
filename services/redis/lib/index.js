const IoRedis = require("ioredis");
const RedLock = require("redlock").default;

/**
 * this class contains all methods needed to connect with a redis server
 * the constructor demands a host and port. If no port is given, the default port 26379 will be used
 */
class Redis
{
    /**
     * @param {string} host
     * @param {number} port
     */
    constructor(host, port=26379, sentinel = true, password = "")
    {
        this.ready = false;

        let options = {
            host: host,
            port: port
        };

        if(sentinel)
        {
            options = {
                sentinels: [
                    {
                        port: port,
                        host: host
                    }
                ],
                name: "mymaster"
            };
        }

        if(password)
        {
            options.sentinelPassword = password;
            options.password = password;
        }

        this.client = new IoRedis(options);
        this.redLock = new RedLock([this.client]);

        this.client.on("ready", () => {
            this.ready = true;
        });

        this.client.on("end", () => {
            this.ready = false;
        });

        this.client.on("error", () => {
            this.ready = false;
        });
    }

    /**
     * @returns {Promise<void>}
     * closes connection immediately, regardless of pending replies
     */
    disconnect()
    {
        return this.client.disconnect();
    }

    /**
     * @returns {Promise<void>}
     * closes connection after all pending replies are resolved
     */
    quit()
    {
        return this.client.quit();
    }

    /**
     * @returns {boolean}
     * Checks if the connection is healthy.
     */
    isReady()
    {
        return this.ready;
    }

    /**
     * @param {string} key
     * @param {any} value JSON-object that gets parsed to a string
     * @returns {Promise<number>}
     * returns Key with value according to the FIFO principle
     */
    insert(key, value)
    {
        return this.insertStr(key, JSON.stringify(value));
    }

    /**
     * @param {string} key
     * @param {any} value The value to set
     * @returns {Promise<number>}
     * returns Key with value according to the FIFO principle
     */
    insertStr(key, value)
    {
        return this.client.rpush(key, value);
    }

    insertFront(key, value)
    {
        return this.client.lpush(key, JSON.stringify(value));
    }

    /**
     * @param {string} key
     * @returns {Promise<string>}
     * deletes and returns the oldest job
     */
    pop(key)
    {
        return this.client.lpop(key);
    }

    /**
     * @param {string} key
     * @returns {Promise<string[]>}
     * deletes and returns a list
     */
    async popEmpty(key)
    {
        const self = this;
        let list;
        await this.redLock.using([key + ":lock"], 5000, async signal => {
            const amount = await self.client.llen(key);

            if (signal.aborted)
            {
                throw signal.error;
            }

            list = await self.client.lpop(key, amount);
        });
        return list;
    }

    /**
     * Return the queue length.
     * @param {string} key
     * @returns {Promise<number>}
     */
    length(key)
    {
        return this.client.llen(key);
    }

    getAll(key)
    {
        return this.client.lrange(key, 0, -1);
    }

    /**
     * @param {string} key the queue in which the value will be stored
     * @param {any} value
     * @returns {Promise<any>}
     * performs a sorted set on a certain queue
     */
    sortedSet(key, value)
    {
        return this.client.zadd(key, Date.now() +  600 * 1000, JSON.stringify(value));
    }

    /**
     * @param {string} key
     * @returns {Promise<string[]>}
     */
    sortedGet(key)
    {
        return this.client.zrange(key,0,-1, "WITHSCORES" );
    }


    /**
     * @param {(...args: any[])=> void} callback
     */
    onErrorRedLock(callback)
    {
        this.redLock.on("error", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onError(callback)
    {
        this.client.on("error", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onConnect(callback)
    {
        this.client.on("connect", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onReady(callback)
    {
        this.client.on("ready", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onDisconnect(callback)
    {
        this.client.on("end", callback);
    }

    /**
     * @param {(...args: any[])=> void} callback
     */
    onReconnect(callback)
    {
        this.client.on("reconnect", callback);
    }
}

module.exports = Redis;
