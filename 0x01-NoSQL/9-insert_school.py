#!/usr/bin/env python3


def insert_school(mongo_collection, **kwargs):
    """insert a new documents"""
    doc = mongo_collection.insert_one(kwargs)
    return doc.inserted_id
