from flask import Flask, request, session, render_template

# 建立 Flask 物件
app = Flask(__name__)
app.secret_key = "hello" # 設定 secret_key

# 根目錄
@app.route("/")
def index():
    return render_template("index.html")

# 用 GET 方法處理 /hello?name=使用者 路徑
@app.route("/hello")
def hello():
    name = request.args.get("name", "")
    session["username"] = name # 將 name 存入 session
    return f"Hello {name}"

# 用 GET 方法處理 /talk 路徑
@app.route("/talk")
def talk():
    name = session["username"]
    return f"If you see this string, that means you successfully stored {name} in session!"

app.run()