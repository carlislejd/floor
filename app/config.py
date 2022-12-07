import pymongo

from os import getenv
from dotenv import load_dotenv


load_dotenv()



def mongo_collection():
    """Returns a collection from the MongoDB database."""
    client = pymongo.MongoClient(getenv('MONGO'))
    db = client.nonfungible 
    return db.globalcontracts