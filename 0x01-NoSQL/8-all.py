#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
    return [i for i in mongo_collection.find()]
