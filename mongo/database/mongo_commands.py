"""This class contains all the methods and functions,
that query or otherwise interact with the mongo database"""
import uuid
import json
import os
from entities.Order import Order
from pymongo import MongoClient

def boot_db():
    """This establishes connection to our mongo db."""
    host = os.environ.get("MONGO_HOST")
    user = os.environ.get("MONGO_USER")
    password = os.environ.get("MONGO_PASSWORD")
    port = os.environ.get("MONGO_PORT")

    dsn = f"mongodb://{user}:{password}@{host}:{port}/?authMechanism=DEFAULT"

    client = MongoClient(dsn, uuidRepresentation="standard")
    mydb = client["DatabaseEksamen"]
    mycol = mydb["Order"]
    return mycol


def insert_order(collection, user_id, products):
    """This inserts an order, it requires a collection,
    id of the user who is creating the order, and what products are in the order."""
    test_myuuid1 = uuid.uuid4()
    order = Order(user_id, str(test_myuuid1), products)
    collection.insert_one(order.return_order())
    return "Succesfully created order"


def get_orders(collection, user_id):
    """This get all orders made by a user, it requires a collection and a user_id."""
    retrieved_data = collection.find_one({"user_id": user_id})
    data = json.dumps(str(retrieved_data))
    return data


def delete_order(collection, order_id):
    """The deletes an order. It requires a collection and the id of the order to be deleted."""
    collection.delete_one({"order_id": order_id})
    return "Successfully deleted order " + order_id


def update_order(collection, order_id, item, new_value):
    """This updates an order, it requires a collection,
    order_id of the order to be deleted,
    the item to be updated, and the new value"""
    collection.update({"order_id": order_id}, {"$set": {item: new_value}})
    return "Successfully updated order " + order_id
