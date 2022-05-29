import ast
import redis
import json
import os
from flask import jsonify

def connect():
        connection = redis.Redis(host = os.environ.get('REDIS_HOST'), 
        port = os.environ.get('REDIS_PORT'))
        return connection

def get_keys_from_dict(item):
        keyList = list(item.keys())
        key = keyList[0]
        return key

def get_values_from_dict(item):
        keyList = list(item.values())
        value = keyList[0]
        return value


def set_summer_products(some_list):
        r = connect()
        pipe = r.pipeline()
        for item in some_list:
                item_key = get_keys_from_dict(item)
                item_value = get_values_from_dict(item)
                print(item_key)
                print(item_value)
                pipe.set(item_key, json.dumps({item_key : item_value}))
                set_response = pipe.execute()
                print("bulk insert response : ", set_response)
        return "Hej"


def get_products_from_redis():
        r = connect()
        my_list = []
        for key in r.scan_iter():
                data = r.get(key)
                my_dict = data.decode("utf-8")
                mydata = ast.literal_eval(my_dict)
                my_list.append(mydata)
        return jsonify(my_list)
