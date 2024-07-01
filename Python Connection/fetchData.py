import sys
import redis

REDIS_PASS = "abc@123"
PORT = 6381
# REDIS_URL = f"redis://localhost:{REDIS_PASS}@myredis:{PORT}"

headers = ['firstname', 'lastname', 'fullname', 'address']

def connect_to_redis():
    try:
        # Can also connect using a specific host, URL, and other details. ↓
        client = redis.StrictRedis(host="localhost", port=PORT, password=REDIS_PASS, decode_responses=True)
        # client = redis.from_url(REDIS_URL)
        print("Connected to Redis server!")
        return client
    except redis.exceptions.ConnectionError as err:
        print(f"Connection error: {err}")
        return None

redis_connection = connect_to_redis()

def retrive_data(key):
    key = str(key)
    try:
      value = redis_connection.get(key)
    except:
      print('An exception occurred')
    return value
    
print(retrive_data(sys.argv[1]))