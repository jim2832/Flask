from flask import Flask, request # 載入 flask 套件

app = Flask(__name__) # 建立 Flask 物件

# 路由裝飾器 -> 建立路徑/對應的處理函式
@app.route("/")

def index(): # 用來回應路徑 / 連線的函式
    print("請求方法: ", request.method) # 列印出 request method
    print("通訊協定: ", request.scheme) # 列印出 request scheme
    print("主機名稱: ", request.host) # 列印出 request host
    print("路徑: ", request.path) # 列印出 request path
    print("完整網址: ", request.url) # 列印出 request url
    
    # headers
    print("瀏覽器和作業系統: ", request.headers.get("User-Agent")) # 列印出 User-Agent
    print("語言偏好: ", request.headers.get("Accept-Language")) # 列印出 Accept-Language
    print("引薦網址: ", request.headers.get("referer")) # 列印出 referer

    # 取得使用者語言偏好
    lang = request.headers.get("Accept-Language")
    print("語言偏好: ", lang)
    if(lang.startswith("en")):
        return "Hello"
    else:
        return "哈囉"
    
# 啟動網站伺服器 (可以透過 port 參數個改 port number)
# 預設 port = 5000
app.run()