from  flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    name="张三"
    age=18
    gender="男"
    return render_template("index.html",**locals())
if __name__ == '__main__':
    app.run(host="192.168.11.12",port=6789,debug=True)