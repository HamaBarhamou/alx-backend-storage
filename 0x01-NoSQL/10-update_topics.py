#!/usr/bin/env python3
"""Using the pymongo module"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school
    document based on the name
    """
    schools_to_update = {'name': name}
    new_values = {'$set': {'topics': topics}}
    mongo_collection.update_many(
        schools_to_update,
        new_values
    )
