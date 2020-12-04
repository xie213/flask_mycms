# -- * -- coding : utf-8 -- * --
from  wtforms.validators import EqualTo,Email,DataRequired,Length
from flask_wtf import FlaskForm
from wtforms import PasswordField,SubmitField,StringField

class RegisterFrom(FlaskForm):
    username = StringField('用户名',validators=[DataRequired(),Length(2,28,message=["用户名必须在2-28之内"])])
    password = PasswordField('密码', validators=[DataRequired(), Length(6, 66, message=["密码必须在6-66之内"])])
    password_equalto = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password',message=["密码不一致"])])
    email = StringField('邮箱',validators=[DataRequired(),Email(message='邮箱格式有误')])
    submit = SubmitField('提交')

