from pymongo import MongoClient
import uuid
from entities.Order import Order
import json
import os 

# This simply boots a collection
def boot_db():
    host = os.environ.get('MONGO_HOST')
    user = os.environ.get('MONGO_USER')
    password = os.environ.get('MONGO_PASSWORD')
    port = os.environ.get('MONGO_PORT')

    dsn = "mongodb://{}:{}@{}:{}/?authMechanism=DEFAULT".format(user, password, host, port)

    client = MongoClient(dsn, uuidRepresentation="standard")
    mydb = client["DatabaseEksamen"]
    mycol = mydb["Order"]
    return mycol


def insert_order(collection, user_id, products):
    test_myuuid1 = uuid.uuid4()
    order = Order(user_id, str(test_myuuid1), products)
    collection.insert_one(order.return_order())


# This finds all orders on user_id
def get_orders(collection, user_id):
    retrieved_data = collection.find_one({"user_id": user_id})
    data = json.dumps(str(retrieved_data))
    return data

#Deletes order by id
def delete_order(collection, order_id):
    collection.delete_one({"order_id": order_id})
    return "Successfully deleted order " + order_id