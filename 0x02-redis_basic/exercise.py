#!/usr/bin/env python3
"""0x02. Redis basic"""
import redis
import uuid


class Cache:
    """
        Create a Cache class. In the __init__ method, store an instance
        of the Redis client as a private variable named _redis (using
        redis.Redis()) and flush the instance using flushdb
    """

    def __init__(self):
        """Initiation object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """the store value in reduce instance"""
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
