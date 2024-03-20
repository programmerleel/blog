# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 15:40
# @Author  : LiShiHao
# @FileName: auth.py.py
# @Software: PyCharm

from app.forms import LoginForm
from app.models import Admin
from flask import Blueprint, render_template
from flask_login import current_user, login_user, login_required, logout_user

# 注册蓝图
auth_blueprints = Blueprint("auth", __name__)

@auth_blueprints.route("/login", methods=["GET","POST"])
def login():
    # 判断是否授权
    if current_user.is_authenticated:
        return render_template('admin/index.html', current_user=current_user)

    login_form = LoginForm()
    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        remember = login_form.remember.data
        # 返回模型对象
        admin = Admin.query.first()
        if admin:
            if username != admin.username:
                msg = "用户名错误"
                return render_template('auth/login.html', login_form=login_form,current_user=current_user,msg=msg)
            elif not admin.check_password(password):
                msg = "密码错误"
                return render_template('auth/login.html', login_form=login_form, current_user=current_user,msg=msg)
            else:
                login_user(admin,remember=remember)
                return render_template('admin/index.html', current_user=current_user)
    return render_template('auth/login.html', login_form=login_form, current_user=current_user)

@auth_blueprints.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template('blog/index.html', current_user=current_user)