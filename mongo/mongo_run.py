import requests
import sys

sys.path.append("mongo")
from functools import wraps
from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from entities.Product import Product
from database.mongo_commands import insert_order, get_orders, boot_db, delete_order, update_order
from utility import user_jwt

from __main__ import app
app.secret_key = "super secret key"

# laver en decorator istedet da det gør det lidt mere reusable
def requires_user(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if not request.headers.has_key("Authorization"):
            print("does not have header")
            return jsonify({"error": "You are not authorized"})

        bearer = request.headers.get("Authorization")
        token = bearer[len("Bearer ") :]

        try:
            decoded = user_jwt.decode_access_token(token)
            session["user_id"] = decoded["sub"]
        except Exception as e:
            print(e)
            return jsonify({"error": "You are not authorized"})

        return f(*args, **kwargs)

    return wrapper


# Just to provide proof of CRUD


@app.route("/mongo", methods=["GET"])
def mongohome():
    return "<h1>HVIS DU SER DETTE SÅ KØRER MONGO SERVEREN</h1>"


# CREATES AN ORDER
@app.route("/mongo/order/create", methods=["POST"])
@requires_user
def create_order():
    user_id = session.get("user_id")
    data = request.get_json()
    list_of_products = []
    for element in data:
        product = Product(
            element["product_id"],
            element["product_name"],
            element["product_brand"],
            element["item_number"],
            element["color"],
            element["grill_type"],
            element["amount_of_burners"],
            element["bread_basket"],
            element["amount_of_wheels"],
            element["length_in_cm"],
            element["width_in_cm"],
            element["product_price"],
        )
        list_of_products.append(product.return_product())

    insert_order(boot_db(), user_id, list_of_products)
    return "Persisted order successfully"

# GET ORDERS BY USER ID
@app.route("/mongo/order", methods=["GET"])
@requires_user
def get():
    return "Returned: " + get_orders(boot_db(), session.get("user_id"))


# DELETES ORDER BY ORDER ID
@app.route("/mongo/order/delete/<id>", methods=["DELETE"])
def delete(id):
    return "Returned: " + delete_order(boot_db(), str(id))

# Updates order by order id
# @app.route("/mongo/order/update/<id>", methods=["UPDATE"])
# def update(id):
#     data = request.get_json()
#     item = data[""]
#     new_item = data[""]
#     return "Returned: " + update_order(boot_db(), str(id), item, new_item)
