from flask import Flask, request, render_template

app = Flask(__name__)

# 根目錄
@app.route("/")
def index():
    return render_template("index.html", name = "Jim") # 將網頁內容轉成 HTML

# calculate
@app.route("/calculate")
def calculate():
    max = request.args.get("max", 0, type = int)
    sum = 0
    for i in range(1, max + 1):
        sum += i
    return render_template("calculate.html", result = sum)

# /show
@app.route("/show")
def show():
    name = request.args.get("name", "") # 取得網址列上的參數
    return f"Hello {name}"

# /page
@app.route("/page")
def page():
    return render_template("page.html")

# 預設 port 是 5000
app.run()