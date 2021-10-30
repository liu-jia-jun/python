# flask 一个python框架，render_template python框架中的一个模块用于模板解析类似于jsp
from flask import Flask,render_template,request

app = Flask(__name__)

# 路由规则，路由不能重复，用户通过唯一路径访问特定的函数
@app.route('/')
def hello_world():  # put application's code here
    return 'Python flask!'


@app.route("/template")
def testTemplate():
    # 通过render_template 来返回给用户渲染后的网页文件
    return render_template("index.html")

@app.route("/user/<name>")
def welcome(name):
    return "你好，%s"%name

# 指定传参类型
@app.route("/user/<int:id>")
def welcome2(id):
    return "你好，%d"%id

# 向页面传递一个变量
@app.route("/test")
def testTemplateAndParams():
    name = ["张三","李四"]
    task = {"任务":"打扫卫生","时间":"3小时"}
    return render_template("index.html",name=name,task=task)


# 表单提交
@app.route("/register")
def register():
    return render_template("register.html")

# 配置接收提交的路由，需要指定method 为post
@app.route("/result",methods=["POST"])
def result():
    if request.method =="POST":
        result = request.form

    return render_template("result.html",result=result)





if __name__ == '__main__':
    app.run()
