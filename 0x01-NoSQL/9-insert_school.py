#!/usr/bin/env python3


def insert_school(mongo_collection, **kwargs):
    """insert a new documents"""
    return mongo_collection.insert_one(kwargs).inserted_id
