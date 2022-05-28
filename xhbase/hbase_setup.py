import happybase
import random
import json
import os
import ast
from .data_generator import product_generator


def connect():
        connection = happybase.Connection(host = os.environ.get('HBASE_HOST'))
        return connection

def create_our_table():
    connection = connect()
    try:
        #Check if you have to specify dictionary 
        connection.create_table("products", {"key": dict()})
    except:
        print("did not create table, as it already exists")

    return connection.table("products")

def populate_table(table):
    batcher = table.batch()
    products = product_generator.return_big_data_products()

    for element in products:
        # number = random.randint(1,100)
        id = element.return_product()["product_id"]    
        #DEN DER FUCKER BYTE FEJL KOMMER HVIS MAN IKKE SMIDER EN DICT BAG PÅ KEY
        column_string = str(f"key:{id}")
        data =  str(element.return_product())
        id_in_bytes = bytes(id, encoding=("utf8"))
        data_in_bytes = bytes(data, encoding=("utf8"))
        batcher.put("summer_product", {column_string: id_in_bytes}, {b'value': data_in_bytes})
    batcher.send()





# b = table.batch()
# b.put(b'row-key-1', {b'cf:col1': b'value1', b'cf:col2': b'value2'})
# b.put(b'row-key-2', {b'cf:col2': b'value2', b'cf:col3': b'value3'})
# b.put(b'row-key-3', {b'cf:col3': b'value3', b'cf:col4': b'value4'})
# b.delete(b'row-key-4')
# b.send()







def run_setup():
    table = create_our_table()
    populate_table(table)

