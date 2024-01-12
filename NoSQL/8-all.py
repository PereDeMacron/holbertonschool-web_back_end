#!/usr/bin/env python3
"""LISTS all document"""

import pymongo


def list_all(mongo_collection): 
    """List all documents"""

    list_documents = mongo_collection.find()
    if list_documents is None:
        return []
    else:
        return list_documents
