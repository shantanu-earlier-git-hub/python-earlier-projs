from typing import TypedDict

from pymongo.synchronous.database import Database

import appmongodb as mongo_db
import models.Product as ProductType

db: Database[[any, ProductType]] = None


def find():
    collection = db['product']
    products = collection.find()
    for product in products:
        print(product)


def find_one():
    collection = db['product']
    one_product = collection.find_one()
    print(one_product)


if __name__ == '__main__':
    client = mongo_db.connect()
    db = client['astrick']
    find()
    mongo_db.close(client)
