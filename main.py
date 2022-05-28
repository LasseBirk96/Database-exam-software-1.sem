import sys
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
sys.path.append("..")
from postGres import postgres_setup
from mongo import mongo_setup
from xhbase import hbase_setup


app = Flask(__name__)
api = Api(app)
#THESE ARE NOT TO BE MOVED
from postGres import postGres_run
from mongo import mongo_run
from xhbase import hbase_run
from xredis import redis_run

@app.route("/home", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER DET</h1>"

if __name__ == "__main__":
    mongo_setup.run_setup()
    postgres_setup.run_setup()
    hbase_setup.run_setup()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False, host='0.0.0.0', port=port)

