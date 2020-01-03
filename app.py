'''
@Author: Linfeng
@Date: 2020-01-03 16:08:57
@LastEditTime : 2020-01-03 16:11:01
@LastEditors  : test
@FilePath: \flask_demo\app.py
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Welcome to Flask world!"