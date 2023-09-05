#!/usr/bin/env python3
""" 10. Change school topics """


def update_topics(mongo_collection, name, topics):
    """ changes all topics of a school document based on the name
        mongo_collection: pymongo collection object
        name: school name to update
        topics: list of topics approached in the school
    """
    if mongo_collection is None:
        return None
    return mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
