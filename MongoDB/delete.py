import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
user_table = client.website.users # 資料庫table

# 刪除特定條件的資料 (也可以用 delete_many 一次刪除多筆資料)
result = user_table.delete_one({"name": "Andy"})

# 取得刪除的結果
print(f"刪除了 {result.deleted_count} 筆資料")

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Update successfully!")
except Exception as e:
    print(e)