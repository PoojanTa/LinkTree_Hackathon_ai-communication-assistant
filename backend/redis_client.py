# Redis connection utility for backend
import redis

# Connect to local Redis instance (default settings)
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def set_value(key, value):
    redis_client.set(key, value)

def get_value(key):
    return redis_client.get(key)
