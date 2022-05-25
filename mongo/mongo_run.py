import sys

sys.path.append("mongo")
from functools import wraps
from flask import Flask, request, jsonify, session
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from entities.Product import Product
from database.mongo_commands import insert_order, get_orders, boot_db, delete_order
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
    p = Product(
        data["product_id"],
        data["product_name"],
        data["product_brand"],
        data["item_number"],
        data["color"],
        data["grill_type"],
        data["amount_of_burners"],
        data["bread_basket"],
        data["amount_of_wheels"],
        data["length_in_cm"],
        data["width_in_cm"],
        data["product_price"],
    )
    insert_order(boot_db(), user_id, p.return_product())
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
