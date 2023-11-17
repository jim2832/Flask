import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
user_table = client.website.users # 資料庫table

# 透過 $and 可以找到多個條件的資料
cursor = user_table.find({"$and": [{"level": 3}, {"password": "123"}]}) # 找出 level 為 1 且 name 為 Tim 的資料
for entry in cursor:
    print(entry["name"])

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Search successfully connected to MongoDB!")
except Exception as e:
    print(e)