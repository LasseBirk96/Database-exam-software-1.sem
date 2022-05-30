"""THIS CONTAINS ALL API ENDPOINTS THAT USE MONGO"""
import ast
import sys
from functools import wraps
from flask import request, jsonify, session
from __main__ import app
from utility import user_jwt
from entities.Product import Product
from database.mongo_commands import insert_order, get_orders, boot_db, delete_order

sys.path.append("mongo")

app.secret_key = "super secret key"


def requires_user(_f):
    """This allows you to lock other actions behind a JWT token"""

    @wraps(_f)
    def wrapper(*args, **kwargs):
        if not request.headers.has_key("Authorization"):
            print("does not have header")
            return jsonify({"error": "You are not authorized"})

        bearer = request.headers.get("Authorization")
        token = bearer[len("Bearer ") :]

        try:
            decoded = user_jwt.decode_access_token(token)
            session["user_id"] = decoded["sub"]
        except Exception as _e:
            print(_e)
            return jsonify({"error": "You are not authorized"})

        return _f(*args, **kwargs)

    return wrapper


@app.route("/mongo", methods=["GET"])
def mongohome():
    """This method simply allows us to test in Insomnia or
    Postman whether or not our mongo service is running"""
    return "<h1>HVIS DU SER DETTE SÅ KØRER MONGO SERVEREN</h1>"


def get_keys_from_dict(item):
    '''This method returns the key from a dict'''
    key_list = list(item.keys())
    key = key_list[0]
    return key


# CREATES AN ORDER
@app.route("/mongo/order/create", methods=["POST"])
@requires_user
def create_order():
    """This receives data from an api call, and allows you to persist order in mongo"""
    user_id = session.get("user_id")
    data = request.get_json()
    list_of_products = []
    for element in data:
        key = get_keys_from_dict(element)
        value = element[key]
        item = ast.literal_eval(value)
        product = Product(
            item["product_id"],
            item["product_name"],
            item["product_brand"],
            item["item_number"],
            item["color"],
            item["grill_type"],
            item["amount_of_burners"],
            item["bread_basket"],
            item["amount_of_wheels"],
            item["length_in_cm"],
            item["width_in_cm"],
            item["product_price"],
        )
        list_of_products.append(product.return_product())
    return insert_order(boot_db(), user_id, list_of_products)


# GET ORDERS BY USER ID
@app.route("/mongo/order", methods=["GET"])
@requires_user
def get():
    """This returns all orders made by whatever user_id is in the JWT token in the API call"""
    return "Returned: " + get_orders(boot_db(), session.get("user_id"))


# DELETES ORDER BY ORDER ID
@app.route("/mongo/order/delete/<id>", methods=["DELETE"])
def delete(_id):
    """This deletes the order that contains the id given in the rest path"""
    return "Returned: " + delete_order(boot_db(), str(_id))
