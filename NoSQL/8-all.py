#!/usr/bin/env python3
""" 8. List all documents in Python """


def list_all(mongo_collection):
    """ lists all documents in a collection
        mongo_collection: pymongo collection object
        Return: empty list if no document in collection
    """
    if mongo_collection is None:
        return []
    return mongo_collection.find()
