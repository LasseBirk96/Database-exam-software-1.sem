'''THIS CLASS CONTAINS ALL API WORK FOR POSTGRES'''
from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from utility import user_jwt
from .database import user_queries, table


@app.route("/postgres", methods=["GET"])
def postgreshome():
    '''This is just a tester, to see if things are running'''
    return "<h1>HVIS DU SER DETTE SÅ KØRER POSTGRES</h1>"


# PERSISTS A USER
@app.route("/postgres/user/persist", methods=["POST"])
def persist_user():
    '''This is the endpoint for persisting a user'''
    data = request.get_json()
    user = user_queries.persist_user(
        data["first_name"],
        data["last_name"],
        data["password"],
        data["age"],
        data["email"],
        data["phonenumber"],
    )
    return jsonify(user)


@app.route("/postgres/user/whoami", methods=["GET"])
def whoami():
    '''This endpoint returns the data of a logged in user'''
    if not request.headers.has_key("Authorization"):
        return jsonify({"error": "You are not authorized"})

    bearer = request.headers.get("Authorization")
    token = bearer[len("Bearer ") :]

    decoded = user_jwt.decode_access_token(token)

    user = user_queries.get_user_by_id(decoded["sub"])

    return jsonify(user)


@app.route("/postgres/user/login", methods=["POST"])
def user_log_in():
    '''This endpoint allows a user to log-in'''
    data = request.get_json()
    user_id = user_queries.user_login(data["email"], data["password"])

    return jsonify(user_jwt.get_access_token(user_id))


# DELETES A USER
@app.route("/postgres/user/delete", methods=["DELETE"])
def delete_user():
    '''This endpoint allows a user to be deleted'''
    data = request.get_json()
    deleted_user = user_queries.delete_user(data["email"])
    return jsonify(deleted_user)


# UPDATES A USER
@app.route("/postgres/user/update", methods=["PUT"])
def update_user():
    '''This endpoints lets a user be updated'''
    data = request.get_json()
    update = user_queries.update_user(data["email"], data["new_phonenumber"])
    return jsonify(update)


# READS A USER
@app.route("/postgres/user/select", methods=["GET"])
def get_user():
    '''This endpoint gets a user from a email'''
    data = request.get_json()
    user = user_queries.get_user(data["email"])
    return jsonify(user)
