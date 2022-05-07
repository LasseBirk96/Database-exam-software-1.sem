from pymongo import MongoClient

client = MongoClient("mongodb://dev:dev@localhost:27017/?authMechanism=DEFAULT")
mydb = client["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)
print(x.inserted_id)
print(client.list_database_names())
client.close()

