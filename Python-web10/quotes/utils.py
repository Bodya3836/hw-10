from pymongo import MongoClient

def get_mongodb():
    client = MongoClient("mongodb+srv://Cluster0:8748@atlascluster.ghgmoal.mongodb.net/hw?retryWrites=true&w=majority")

    db = client.hw
    return db