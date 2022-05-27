import sys

sys.path.append("mongo")
from pymongo import MongoClient
import uuid
from entities.Product import Product
from database.mongo_commands import insert_order, boot_db

def generate_lists_with_data():
    # All products have the same UUID right now, this is just a test thing, this will change
    test_myuuid = uuid.uuid4()

    product = Product(
        "1",
        test_myuuid,
        "1",
        "Grill",
        "asd",
        "2",
        "black",
        "gas",
        "3",
        "yes",
        "4",
        "75",
    )
    second_product = Product(
        "2",
        test_myuuid,
        "2",
        "Cool Grill",
        "qwe",
        "2",
        "black",
        "gas",
        "3",
        "yes",
        "4",
        "75",
    )
    third_product = Product(
        "3",
        test_myuuid,
        "3",
        "Lit Grill",
        "fd",
        "2",
        "black",
        "gas",
        "3",
        "yes",
        "4",
        "75",
    )
    fourth_product = Product(
        "4",
        test_myuuid,
        "4",
        "Awesome Grill",
        "Wwefweber",
        "2",
        "black",
        "gas",
        "3",
        "yes",
        "4",
        "75",
    )
    fifth_product = Product(
        "5",
        test_myuuid,
        "76",
        "asdasdasdasd Grill",
        "Wwefweber",
        "2",
        "asdasdasd",
        "gas",
        "3",
        "asasd",
        "4",
        "75",
    )

    list_of_products = []
    list_of_products.append(product.return_product())
    list_of_products.append(second_product.return_product())

    list_of_more_products = []
    list_of_more_products.append(third_product.return_product())
    list_of_more_products.append(fourth_product.return_product())

    test_list = []
    test_list.append(fifth_product.return_product())

    return list_of_products, list_of_more_products, test_list


# Inserter order, works well, does need some tunning in the future


# This runs the test, creates a db and populates it
def run_setup():
    generated_lists = generate_lists_with_data()
    insert_order(boot_db(), 1, generated_lists[0])
    insert_order(boot_db(), 2, generated_lists[1])
    insert_order(boot_db(), 3, generated_lists[2])


