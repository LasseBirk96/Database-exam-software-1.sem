from database import table, user_queries


from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from pymongo import MongoClient


app = Flask(__name__)
api = Api(app)


@app.route("/postgres", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER POSTGRES</h1>"


# PERSISTS A USER
@app.route("/postgres/user/persist", methods=["POST"])
def persist_user():
    data = request.get_json()
    user_queries.persist_user(data["first_name"], data["last_name"], data["password"], data["age"], data["email"], data["phonenumber"])
    return "Persisted user successfully"

# DELETES A USER
@app.route("/postgres/user/delete", methods=["DELETE"])
def delete_user():
    data = request.get_json()
    user_queries.delete_user(data["email"])
    return "Deleted user successfully"

# UPDATES A USER
@app.route("/postgres/user/update", methods=["PUT"])
def update_user():
    data = request.get_json()
    user_queries.update_user(data["email"], data["new_phonenumber"])
    return "Updated user successfully"

# READS A USER
@app.route("/postgres/user/select", methods=["GET"])
def get_user():
    data = request.get_json()
    user_queries.get_user(data["email"])
    return "Selected user successfully"

# GET ORDERS BY USER ID
# @app.route("/order/<id>", methods=["GET"])
# def get(id):
#     return "Returned: " + get_orders(boot_db(), int(id))


if __name__ == "__main__":
    app.run()
