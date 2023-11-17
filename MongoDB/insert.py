import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

# 創建一個 client
client = MongoClient(uri, server_api=ServerApi('1'))

# 創建一個 database (website)
db = client.website

# 創建一個 collection (users)
collection = db.users

# 在 collection 中新增一筆資料
# result = collection.insert_one({"name": "Sam", 
#                        "email":"Sam@gmail.com", 
#                        "password":"123", 
#                        "level":2}
#                        )

# 在 collection 中新增多筆資料
result = collection.insert_many([{"name": "Tim", "email":"Tim@gmail.com", "password":"123", "level":1}, 
                               {"name": "Andy", "email":"Andy@gmail.com", "password":"123", "level":3}]
                               )

# 取得新增資料的 ID
print(result.inserted_ids)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)