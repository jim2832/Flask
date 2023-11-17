import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
user_table = client.website.users # 資料庫table

# 找到特定id的資料 (find_one 為找到第一筆資料)
# data = user_table.find_one({"_id": ObjectId("65572a3d38baa64581c1059e")})
# print(data["name"])

# 找到特定條件的資料
cursor = user_table.find({"level": 1}) # 找出 level 為 1 的資料
print(cursor) # 資料筆數
for entry in cursor:
    print(entry["name"])

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Search successfully connected to MongoDB!")
except Exception as e:
    print(e)