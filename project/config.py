import pymongo

from os import getenv
from dotenv import load_dotenv


load_dotenv()



def contract_collection():
    """Returns a collection from the MongoDB database."""
    client = pymongo.MongoClient(getenv('MONGO'))
    db = client.floor
    return db.contractIds


def prices_collection():
    """Returns a collection from the MongoDB database."""
    client = pymongo.MongoClient(getenv('MONGO'))
    db = client.floor
    return db.prices