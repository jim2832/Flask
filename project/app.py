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


# 註冊頁面 
@app.route("/signup", methods=["POST"])
def signup():
    # 取得表單資料
    username = request.form.get("username")
    password = request.form.get("password")

    # 檢查帳號是否已經被註冊
    user = db.users.find_one({"username": username})
    if user:
        return redirect("/system_msg?message=帳號已經被註冊！")
    
    # 儲存帳號密碼
    db.users.insert_one({ "username": username, "password": password})

    # 註冊成功，轉到登入頁面
    return redirect("/system_msg?message=註冊成功！")


# 登入頁面
@app.route("/signin", methods=["POST"])
def signin():
    # 取得表單資料
    username = request.form.get("username")
    password = request.form.get("password")

    # 檢查帳號密碼是否正確
    user = db.users.find_one({"$and": [{"username": username}, {"password": password}]})
    if user:
        # 設定 session
        session["username"] = username
        return redirect("/member")
    else:
        return redirect("/system_msg?message=帳號或密碼輸入錯誤！")
    
# 登出頁面
@app.route("/signout")
def signout():
    # 清除 session
    del session["username"]
    return redirect("/")


# 會員頁面
@app.route("/member")
def member():
    # 檢查是否有登入
    if "username" in session:
        return render_template("member.html")
    else:
        return redirect("/")


# 系統訊息
@app.route("/system_msg")
def error():
    message = request.args.get("message", "發生不明錯誤")
    return render_template("system_msg.html", message=message), {"Refresh": "2 ; url= / "}


app.run(port=3000)