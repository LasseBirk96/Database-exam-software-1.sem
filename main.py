import sys
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
sys.path.append("..")


app = Flask(__name__)
api = Api(app)
#THESE ARE NOT TO BE MOVED
from postGres import postGres_run
from mongo import mongo_run

@app.route("/home", methods=["GET"])
def home():
    return "<h1>HVIS DU SER DETTE SÅ KØRER DET</h1>"

if __name__ == "__main__":
    print(os.environ.get('MY'))
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
