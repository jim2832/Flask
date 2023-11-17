import pymongo # Importing the pymongo library

# 連線到 MongoDB 雲端資料庫
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from bson.objectid import ObjectId

password = "newfish2832"
uri = f"mongodb+srv://root:{password}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
user_table = client.website.users # 資料庫table

# 更新特定id的資料(單筆)
user_table.update_one({"name": "Jim"}, {"$set": {"password": "123"}}) # 將密碼改為 123
user_table.update_one({"name": "Jim"}, {"$inc": {"level": 1}}) # level + 1

# 更新特定條件的資料(多筆)
result = user_table.update_many({"level": 1}, {"$set": {"level": 6}}) # 將 level 為 2 的資料，改為 level 4

# 若本來沒有這欄位，則會新增
# user_table.update_one({"name": "Jim"}, {"$set": {"des": "hi"}})

# 不同的更新方式
# 1. $set(覆蓋/新增)
# 2. $inc(數字相加)
# 3. $mul(數字相乘)
# 4. $rename(重新命名)
# 5. $unset(刪除)

# 取得更新的結果
print(f"找到 {result.matched_count} 筆資料") # 找到幾筆資料
print(f"更新 {result.modified_count} 筆資料") # 更新幾筆資料

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Update successfully!")
except Exception as e:
    print(e)