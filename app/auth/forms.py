#encoding=utf-8
'''
Created on 2017��4��11��

@author: Administrator
'''
from flask_wtf import Form
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import Required,Length,Email

class LoginForm(Form):
    email=StringField('Email',validators=[Required(),Length(1,64),Email()])
    password=PasswordField('Password',validator=[Required()])
    remember_me=BooleanField('Keep me logged in')
    submit=SubmitField('Log In')
