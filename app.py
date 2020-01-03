'''
@Author: Linfeng
@Date: 2020-01-03 16:08:57
@LastEditTime : 2020-01-03 17:18:01
@LastEditors  : test
@FilePath: \flask_demo\app.py
'''

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    '''
    修改返回的数据内容,使用html标记
    '''
    return "<h1>Welcome to Flask world!</h1><img src='https://github.com/jeffsui/app_image_resource/blob/master/20200103_cold.jpg?raw=true'></img>"

if __name__ == "__main__":
    DEBUG = True #设置DEBUG模式,不用频繁启动服务
    PORT =5000 #指定端口
    app.run(port=PORT,debug=DEBUG) #使用app.run()启动