#!/usr/bin/env python3
"""
This script serves as the main entry point for a Python application utilizing
Redis caching.
"""
import uuid
import redis
from typing import Union, Optional


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
    def __init__(self) -> None:
        """ Initialization"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis database"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[callable] = None
            ) -> Union[str, bytes, int, float]:
        """Get data from redis database"""
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, data: bytes) -> str:
        """Convert bytes to string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """Convert bytes to int"""
        return int.from_bytes(data, byteorder='big')
