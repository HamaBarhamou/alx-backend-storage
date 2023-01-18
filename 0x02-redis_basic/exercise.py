import redis
import uuid
"""Redis class"""


class Cache:
    _redis = None

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = str(uuid.uuid1())
        self._redis.mset({key: data})
        return key