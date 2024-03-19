#!/usr/bin/env python3
"""
This script serves as the main entry point for a Python application utilizing
Redis caching.
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    A simple cache implementation using Redis.

    Attributes:
        _redis (redis.Redis): A Redis client instance.

    Methods:
        __init__(): Initializes the Cache object and connects to Redis.
        store(data: Union[str, bytes, int, float]) -> str:
            Stores data in Redis with a random key and returns the key.
    """
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


cache = Cache()
key = cache.store("example data")
print("Stored data with key:", key)
