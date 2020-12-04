# -- * -- coding : utf-8 -- * --
from flask import Blueprint,render_template,redirect,url_for,request

from App.extension import db
from App.user.forms import RegisterFrom
from App.user.models import User
from utlis import restful
from utlis.email import send_email

user = Blueprint('user',__name__)

def get_error(form):
    message = form.error.popitem()[1][0]
    return message


@user.route('/register/',methods = ['POST','GET'])
def register():
    if request.method == 'POST':
        form = RegisterFrom(request.form)
        if form.validate():
            password = form.password1.data
            email = form.email.data
            e = User.query.filter(User.email == email).first()
            if e:
                return restful.RestfulResult('对不起,该用户已存在！')
            user = User(password=password,email=email)
            db.session.add(user)
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(message=get_error(form))
    return render_template('user/register.html')

@user.route('/activate/<token>',methods = ['POST','GET'])
def activate(token):
    if User.check_token(token):
        return redirect(url_for('user.login'))
    else:
        return redirect(url_for('user/register'))

@user.route('/login/',methods = ['POST','GET'])
def login():
    return '登录'

@user.route('/index/',methods = ['POST','GET'])
def index():
    return 'index'