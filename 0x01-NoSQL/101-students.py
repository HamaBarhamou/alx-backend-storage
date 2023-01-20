#!/usr/bin/env python3
"""using the pymongo module"""


def top_students(mongo_collection):
    """
    returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {'$project': {
            'name': 1,
            'averageScore': {'$avg': '$topics.score'}
        }},
        {'$sort': {'averageScore': -1}}
    ])
