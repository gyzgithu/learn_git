from  flask import Flask,render_template
app=Flask(__name__)
book={
    "name":"三体",
    "author":"刘慈欣",
    "article":[{
        "id":101,
        "titile":"第一章",
        "content":"地球往事"
    },
{       "id":102,
        "titile":"第二章",
        "content":"黑暗森林"
    },
{       "id":103,
        "titile":"第三章",
        "content":"死神永生"
    },

]
}
@app.route("/")
def index():
    articles=book["article"]
    return  render_template("index.html",**locals())


@app.route("/<int:pk>")
def detail(pk):
    article=None
    for a in book["article"]:
        if a["id"]==pk:
            article=a

    return  render_template("detail.html",**locals())



if __name__ == '__main__':
    app.run(debug=True)