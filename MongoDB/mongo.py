import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

# 創建一個 client
client = MongoClient(uri, server_api=ServerApi('1'))

# 創建一個 database
db = client.account

# 創建一個 collection
collection = db.users

# 在 collection 中新增一筆資料
# result = collection.insert_one({"name": "Jim","age": 24}
#                                )

# 在 collection 中新增多筆資料
result = collection.insert_many([{"name": "Tom","age": 25},
                                 {"name": "John","age": 26},
                                 {"name": "Mary","age": 27}]
                                )

# 取得新增資料的 ID
print(result.inserted_ids)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)