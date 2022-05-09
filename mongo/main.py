from pymongo import MongoClient
import uuid 
import sys
sys.path.append("..")
from mongo.entities import order_entity 
from mongo.entities import product_entity 

myuuid = uuid.uuid4()

client = MongoClient("mongodb://dev:dev@localhost:27017/?authMechanism=DEFAULT")
mydb = client["mydatabase"]
mycol = mydb["customers"]


#x = mycol.insert_one(mydict)
#print(x.inserted_id)
print(mydb.list_collection_names())
for x in mycol.find():
    print(x)




#mycol.insert_many(my_list)

      
def insert_order(user_id, uuid, product_id, product_name, product_brand, item_number, color, grill_type, amount_of_burners, bread_basket, amount_of_wheels, length_in_cm, width_in_cm, product_price):
    product = product_entity(
        product_id, 
        product_name, 
        product_brand, 
        item_number, 
        color, 
        grill_type, 
        amount_of_burners, 
        bread_basket, 
        amount_of_wheels, 
        length_in_cm, 
        width_in_cm, 
        product_price
        )

    order = order_entity(user_id, str(uuid), [product]
    )

    mycol.insert_many(order)

def get_orders(collection, user_id):
    print(collection.find_one({"user_id": user_id}))

get_orders(mycol, "1") 


insert_order("3", myuuid, "1", "Grill", "Weber", "2", "black", "gas", "3", "yes", "4", "75", "95", "9999")



client.close()