#!/usr/bin/env python3
"""Update topics"""

import pymongo


def update_topics(mongo_collection, name, topics):
    """Update the topics"""
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
