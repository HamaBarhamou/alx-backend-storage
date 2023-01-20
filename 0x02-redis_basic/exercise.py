#!/usr/bin/env python3
"""redis basic"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    decorator that takes a single method
    argument and returns it
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        increments a key with the method's name in db
        everytime it's called
        """
        if self._redis.get(key) is None:
            self._redis.set(key, 0)
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    decorator to store the history of inputs and outputs
    for a particular function
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """stores method's inputs and outputs into redis lists"""
        self._redis.rpush(f'{key}:inputs', str(args))
        output = method(self, *args, **kwds)
        self._redis.rpush(f'{key}:outputs', str(output))
        return output
    return wrapper


def replay(method: Callable) -> None:
    """
    prints the call history of the method passed
    as parameter
    """
    r_instance = method.__self__._redis
    key = method.__qualname__
    n_calls = r_instance.get(key).decode("utf-8")
    print(f'{key} was called {n_calls} times:')
    fn_inputs = r_instance.lrange(f'{key}:inputs', 0, -1)
    fn_outputs = r_instance.lrange(f'{key}:outputs', 0, -1)
    fn_inout = list(zip(fn_inputs, fn_outputs))
    for input, output in fn_inout:
        input = input.decode('utf-8')
        output = output.decode('utf-8')
        print(f"{key}(*{input}) -> {output}")


class Cache:
    """class to create a new redis instance and store data into it"""
    def __init__(self):
        """instantiates new redis instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores new data with unique id into instance"""
        id = str(uuid.uuid4)
        self._redis.set(id, data)
        return id

    def get(self, key: str, fn: Callable = None):
        """
        take a key string argument and an optional
        Callable argument named fn that will be used
        to convert the data back to the desired format.

        Conserve original get behavior if key doesn't exists
        """
        val = self._redis.get(key)
        if fn is not None:
            return fn(val)
        return val

    def get_str(self, key: str) -> str:
        """parametrize Cache.get to str"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """parametrize Cache.get to int"""
        try:
            val = int(self._redis.get(key))
        except ValueError:
            val = 0
        return val
