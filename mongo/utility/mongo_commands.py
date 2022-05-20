from pymongo import MongoClient
import uuid
from entities.Order import Order
import json

# This simply boots a collection
def boot_db():
    client = MongoClient(
        "mongodb://dev:dev@localhost:27017/?authMechanism=DEFAULT",
        uuidRepresentation="standard",
    )
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