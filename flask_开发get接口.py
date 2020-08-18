#coding=utf-8
#flask开发get接口
from flask import Flask
from flask import request
import json
app = Flask(__name__)
@app.route('/')
def Home():
    data=json.dumps({"username":"Mushishi_xu","password":"111111"})
    return data


@app.route('/passport/user/login',methods=['GET'])
def Login():
    username=request.args.get("username")
    password=request.args.get("password")
    if username and password:
      data = json.dumps({"username": username,
                       "password": password,
                       "code": "200",
                       "message": "登陆成功",
                       "info": "www.Imooc.com"})
    else:
        data = json.dumps({"message":"请传递参数"})
    return data


if __name__ == "__main__":
    app.run()