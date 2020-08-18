#coding=utf-8
#flask开发post接口
from flask import Flask
from flask import request
import json
app = Flask(__name__)
@app.route('/')
def Home():
    data=json.dumps({"username":"Mushishi_xu","password":"111111"})
    return data


@app.route('/passport/user/post_login',methods=['POST'])
def post_login():
    request_method = request.method
    if request_method == 'POST':
        username=request.form.get("username")
        password=request.form.get("password")
        data = json.dumps({"username": username,
                           "password": password,
                           "code":"200",
                           "message":"登陆成功",
                           "info":"www.Imooc.com"})

    else:
        data = json.dumps({"message":"请求不合法"})
    return data


if __name__ == "__main__":
    app.run()