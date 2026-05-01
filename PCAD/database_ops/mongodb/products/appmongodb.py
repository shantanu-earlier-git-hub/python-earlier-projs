from pymongo import MongoClient

url = "mongodb://localhost:27017/"


def connect():
    try:
        client = MongoClient(url)
    except Exception as e:
        print("Failed to connect to MongoDB", e.args)
    return client


def close(client: MongoClient):
    try:
        client.close()
        print("Connection closed")
    except Exception as e:
        print("Failed to close connection", e.args)
