import redis

REDIS_PASS = "abc@123"
PORT = 6380
REDIS_URL = f"redis://localhost:{REDIS_PASS}@myredis:{PORT}"

def connect_to_redis():
    try:
        # Can also connect using a specific host, URL, and other details. ↓
        client = redis.StrictRedis(host="localhost", port=PORT, password=REDIS_PASS)
        # client = redis.from_url(REDIS_URL)
        print("Connected to Redis server!")
        return client
    except redis.exceptions.ConnectionError as err:
        print(f"Connection error: {err}")
        return None

redis_connection = connect_to_redis() 

if redis_connection:
    print(f"Connection Details: {redis_connection} \n")
    redis_connection.set("Day", "Friday", ex=1500)
    value = redis_connection.get("Day")
    print(f"Retrieved value: {value.decode('utf-8')}")
    
    # # Close the connection (optional)
    redis_connection.close()
    print("Connection closed.")