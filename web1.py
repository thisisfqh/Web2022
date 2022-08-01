#!/usr/bin/env python
# -- coding: utf-8 --
# @time : 2022/7/13  15:02
# @Author : fqh
# @File : web1.py
from flask import Flask, render_template, request
from requests import Request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/test1")
def test1():
    return render_template("test1.html")


@app.route("/test2")
def test2():
    return render_template("test2.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route('/loginProcess', methods=['POST', 'GET'])
def loginProcesspage():
    if request.method == 'POST':
        nm = request.form['nm']  # 获取姓名文本框的输入值
        pwd = request.form['pwd']  # 获取密码框的输入值
        if nm == 'cao' and pwd == '123':
            return render_template("index.html")  # 使用跳转html页面路由
        else:
            return 'the username or userpwd does not match!'

@app.route('/buildtomirror')
def buildtomirror():
    return "ok"

@app.route('/buildtotar')
def buildtotar():
    return "ok"


if __name__ == '__main__':
    app.run(
        host="127.0.0.1",
        port=3333,
        debug=True
    )
