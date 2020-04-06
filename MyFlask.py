from flask import Flask,render_template,request
import jieba

app = Flask(__name__)


# @app.route('/')
# def start():
#     response='动态数据'
#     return render_template('hello.html',msg=response)    #msg为传递给hello.htmi的参数 接收传递过去的动态数据 msg这个参数名要保持一致


@app.route('/')
def start():
    return render_template('login.html')

@app.route('/login',methods=['POST'])
def login():
    u = request.form.get('username')
    p = request.form.get('pwd')
    # request.args.get()   get通过这种方式接收参数，获得数据
    #select * from users where username = %s and password = %s   关联数据库
    #print(u,p)
    if u=='zhang' and p == '1234':
     return '登录成功'
    else:
     return render_template('login.html',msg='登录失败')     #msg动态传递参数


if __name__ == '__main__':
    app.run()