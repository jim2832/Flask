from flask import Flask, request # 載入 flask 套件

app = Flask(__name__) # 建立 Flask 物件

# 建立路徑 /getSum 連線的處理函式
# 利用 query string 提供彈性 -> /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum(): # 1+2+3+...+max
    sum = 0
    min = int(request.args.get("min", 1)) # 取得 query string 中的 min 參數 (預設值為 1)
    max = int(request.args.get("max", 100)) # 取得 query string 中的 max 參數 (預設值為 100)
    for i in range(min, max+1):
        sum += i
    return "總和: " + str(sum) # 將總和轉成字串後回傳

@app.route("/")
def index():
    return "Hello"

app.run()