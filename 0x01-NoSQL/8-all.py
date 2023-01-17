#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    """the function return the all collections in mongodb databases"""
    return [i for i in mongo_collection.find()]
