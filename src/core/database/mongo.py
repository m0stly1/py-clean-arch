import pymongo
import os

db_url =  os.getenv("DB_URL")

class Mongodb(object):
    @classmethod
    def create_connection(cls):
        db_connection = pymongo.MongoClient(db_url)
        return db_connection["stock_se"]
