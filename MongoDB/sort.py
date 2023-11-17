import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
user_table = client.website.users # 資料庫table

# 透過 sort 可以對資料進行排序
cursor = user_table.find({"name": "Andy"}).sort("level", pymongo.DESCENDING) # 將 level 由大到小排序
cursor = user_table.find({}, sort = [("level", pymongo.DESCENDING), ("name", pymongo.ASCENDING)]) # 將 level 由大到小排序，若 level 相同，則將 name 由小到大排序
for entry in cursor:
    print(entry)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Search successfully connected to MongoDB!")
except Exception as e:
    print(e)