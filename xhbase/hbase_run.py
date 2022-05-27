from __main__ import app
import json
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from database import hbase_commands



@app.route("/hbase", methods=["GET"])
def hbasehome():
    return "<h1>HVIS DU SER DETTE SÅ KØRER HBASE</h1>"


@app.route("/hbase/summerproducts/", methods=["GET"])
def get_all_summer_products():
    connection = hbase_commands.connect()
    table = connection.table("products")
    rows = table.rows([b"summer_product"])
    for key, data in rows:
        return str(data)
