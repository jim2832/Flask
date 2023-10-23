from flask import Flask

# 所有在 static_folder 資料夾底下的檔案，都對應到網址路徑 static_url_path
app = Flask(__name__,
            static_folder = "static", #靜態資料夾
            static_url_path = "/" #靜態網址名稱
            )

# 路由裝飾器 -> 建立路徑/對應的處理函式
@app.route("/")
def index(): # 用來回應路徑 / 連線的函式
    return "Hello world, this is a test." # 回傳網站首頁的內容

app.run()