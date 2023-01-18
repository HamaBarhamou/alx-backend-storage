#!/usr/bin/env python3
import redis
import uuid
"""Redis class"""


class Cache:
    """Redis class implementation"""
    _redis = None

    def __init__(self):
        """Initiation object"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        """the store value in reduce instance"""
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key
