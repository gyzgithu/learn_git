from flask import Flask, render_template, url_for, redirect, request,session

app = Flask(__name__)
book = {
    "name": "三体",
    "author": "刘慈欣",
    "article": [{
        "id": 101,
        "titile": "第一章",
        "content": "地球往事"
    },
        {"id": 102,
         "titile": "第二章",
         "content": "黑暗森林"
         },
        {"id": 103,
         "titile": "第三章",
         "content": "死神永生"
         },

    ]
}
users=[
    {"email":"163@163.com",
     "passworld":"1"},
    {"email":"1631@163.com",
     "passworld":"1"},

]
app.secret_key="ccwpxclsac;s[xwxd;q[xwnnmp["


@app.route("/")
def index():
    global currentuser
    user = currentuser
    articles = book["article"]
    return render_template("index.html", **locals())


@app.route("/<int:pk>")
def detail(pk):
    global currentuser
    user = currentuser
    article = None
    for a in book["article"]:
        if a["id"] == pk:
            article = a

    return render_template("detail.html", **locals())



@app.route("/login", methods=["GET", "POST"])
def login():
    global currentuser
    if request.method == "GET":
        return render_template("login.html", **locals())
    elif request.method == "POST":
        user = None
        email = request.form.get("email")
        password = request.form.get("password")
        for u in users:
            if u["email"] == email and u["password"] == password:
                session["email"]=user
                return redirect(url_for("index"))
        print("登录失败")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():
    global currentuser
    session.pop("user")
    return redirect(url_for("index"))


@app.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html", **locals())
    elif request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        global users
        users.append({
            "email": email,
            "password": password
        })
        print("当前用户有", users)
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
