# 初始化資料庫
import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

PASSWORD = "newfish2832"
uri = f"mongodb+srv://root:{PASSWORD}@mydatabase.kue6vpz.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client.MemberSystem
                         
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# 初始化後端伺服器
from flask import *
app = Flask(__name__,
            static_folder = "public",
            static_url_path="/"
            )
app.secret_key = "123" # 設定一組密碼鑰匙

# 設定網站首頁
@app.route("/")
def home():
    return render_template("index.html")

# 會員頁面
@app.route("/member")
def member():
    return render_template("member.html")

# 錯誤頁面
@app.route("/error")
def error():
    message = request.args.get("message", "發生不明錯誤")
    return render_template("error.html", message=message)

app.run(port=3000)