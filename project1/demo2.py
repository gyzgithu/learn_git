from flask import Flask
app=Flask(__name__)
@app.route("/")
def index():
    return "欢迎来到flask首页"
@app.route("/<int:pk>")
def detail(pk):
    return f"欢迎来到flask第{pk}页"
if __name__ == '__main__':
    app.run(host="192.168.11.12",port=6789,debug=True)