from __main__ import app
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from .database import redis_commands


@app.route("/redis", methods=["GET"])
def redishome():
    return "<h1>HVIS DU SER DETTE SÅ KØRER REDIS</h1>"



# @app.route("/redis/test", methods=["POST"])
# def redistest():
#     data = request.get_json()
#     redis_commands.set_summer_products(data)
#     return "<h1>HVIS DU SER DETTE SÅ KØRER REDIS</h1>"







