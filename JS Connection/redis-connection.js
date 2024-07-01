const PORT = 6380;
const redisUrl = `redis://localhost:${PORT}`;

const redis = require('redis');

async function main() {
    const client = redis.createClient({
        url: redisUrl,
        password: 'abc@123'
    });
    

    client.on('error', (err) => {
        console.error('Redis Client Error:', err);
        throw new Error(`Redis Server is not available on port: ${PORT}`);
    });

    try {
        await client.connect();
        console.log("Connected to Redis server!");
        console.log("Connection Details");
        console.table(client);
    } catch (err) {
        console.error('Failed to connect to Redis:', err);
        return;
    }

    try {
        await client.set('Month', 'June', {
            EX: 1500
        });
        const value = await client.get('Month');
        console.log('Month:', value);
    } catch (err) {
        console.error('Error performing Redis operations:', err);
    } finally {
        await client.quit();
        console.log("Connection Closed");
    }
}

main().catch(err => {
    console.error('Unexpected error:', err);
    process.exit(1);
});