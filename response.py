from flask import Flask, request, redirect
import json

app = Flask(__name__)

@app.route("/")
def index():
    lang = request.headers.get("accept-language")
    print("語言偏好: ", lang)
    if(lang.startswith("en")):
        return redirect("/en")
    else:
        return redirect("/zh")

# 英文版
@app.route("/en")
def index_english():
    # json.dumps() -> 將 Python 物件轉成 JSON 字串
    return json.dumps({"status": "ok", "message": "Hello"},
                      ensure_ascii=False) # ensure_ascii=False -> 不要將中文字轉成 unicode

# 中文版
@app.route("/zh")
def index_chinese():
    return json.dumps({"status": "ok", "message": "哈囉"},
                      ensure_ascii=False)
    
@app.route("/redirect")
def redirect_to_index():
    return redirect("https://www.google.com") # 將網址導向 Google

app.run()