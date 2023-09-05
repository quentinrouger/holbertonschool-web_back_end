#!/usr/bin/env python3
"""" 9. Insert a document in Python """


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection based on kwargs
        mongo_collection: pymongo collection object
        kwargs: key-value pairs to insert in the document
        Return: new _id
    """
    if mongo_collection is None:
        return None
    return mongo_collection.insert_one(kwargs).inserted_id
