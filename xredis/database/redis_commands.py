import redis
import json
import os


def connect():
        connection = redis.Redis(host = os.environ.get('REDIS_HOST'), 
        port = os.environ.get('REDIS_PORT'))
        return connection


def set_summer_products(some_list):
        r = connect()
        pipe = r.pipeline()
        # data_list = [{"key":"1", "value":"apple"},
        #         {"key":"2", "value":"mango"},
        #         {"key":"3", "value":"grapes"},
        #         {"key":"4", "value":"orange"},
        #         {"key":"5", "value":"pineapple"},
        #         {"key":"6", "value":"guava"},
        #         {"key":"7", "value":"watermelon"}]

        for item in some_list:
                pipe.set(item['key'], json.dumps({item['key'] : item['value']}))
                set_response = pipe.execute()
                print("bulk insert response : ", set_response)
        return "Hej"


