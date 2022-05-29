import happybase
import random
import os
from .data_generator import product_generator


def connect():
        connection = happybase.Connection(host = os.environ.get('HBASE_HOST'))
        return connection

def create_our_table():
    connection = connect()
    try:
        #Check if you have to specify dictionary 
        connection.create_table("products", {"cf:": dict()})
    except:
        print("did not create table, as it already exists")

    return connection.table("products")


def populate_table(table):
    batcher = table.batch()
    products = product_generator.return_big_data_products()
    number = 1
    for element in products:
        column_string = str(f"cf:{number}")
        number = random.randint(1,100)
        if number == 4:
             batcher.put(b"summer_product", {column_string: str(element.return_product())})
             number = number + 1
        batcher.put(b"product", {column_string: str(element.return_product())})
        number = number + 1
    batcher.send()






def run_setup():
    table = create_our_table()
    populate_table(table)

