from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient
from entities.Order import Order
from entities.Product import Product
from utility.mongo_commands import insert_order, get_orders, boot_db

app = Flask(__name__)
api = Api(app)


@app.route("/", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER SERVEREN</h1>"


# CREATES AN ORDER
@app.route("/order/create", methods=["POST"])
def create_order():
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
    insert_order(boot_db(), 7, p.return_product())
    return "Persisted order successfully"


# GET ORDERS BY USER ID
@app.route("/order/<id>", methods=["GET"])
def get(id):
    return "Returned: " + get_orders(boot_db(), int(id))


if __name__ == "__main__":
    app.run()
