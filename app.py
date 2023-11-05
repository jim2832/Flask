from flask import Flask
app = Flask(__name__)

# 路由裝飾器 -> 建立路徑/對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 連線的函式
    return "Hello world, this is a test." # 回傳網站首頁的內容

"""
@app.route("/data")
def getData():
    return "Data here"
"""

# 動態路由設定 用<>來包起參數
@app.route("/user/<name>")
def getData(name):
    if(name == "jim"):
        return "Hello there " + name
    else:
        return "Hello " + name
        

# 啟動網站伺服器 (可以透過 port 參數個改 port number)
# 預設 port = 5000
app.run()