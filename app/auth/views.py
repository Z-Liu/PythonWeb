#encoding=utf-8
'''
Created on 2017Äê4ÔÂ11ÈÕ

@author: Administrator
'''
from flask import render_template
from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')