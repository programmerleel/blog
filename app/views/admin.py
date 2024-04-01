# -*- coding: utf-8 -*-
# @Time    : 2024/3/20 22:27
# @Author  : Lee
# @Project ：blog-master 
# @File    : admin.py
import json

# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 15:40
# @Author  : LiShiHao
# @FileName: auth.py.py
# @Software: PyCharm

from flask import Blueprint, render_template,request,redirect
from flask_login import login_required, current_user

from app import db, csrf
from app.models import Category

# 注册蓝图
admin_blueprints = Blueprint("admin", __name__)

@admin_blueprints.route("/index", methods=["GET","POST"])
@login_required
def login():
    # 跳转管理界面
    return render_template('admin/index.html', current_user=current_user)

@admin_blueprints.route("/edit", methods=["GET","POST"])
@login_required
def edit():
    categories = Category.query.all()
    return render_template('admin/edit.html', categories=categories,current_user=current_user)






@admin_blueprints.route("/category", methods=["GET","POST"])
@login_required
def category():
    categories = Category.query.all()
    return render_template('admin/category.html',categories=categories, current_user=current_user,msg="")

@csrf.exempt
@admin_blueprints.route("/alter_category", methods=["POST"])
@login_required
def alter_category():
    data = json.loads(request.form.get('data'))
    id = int(data['id'])
    name = data['name']
    category = Category.query.filter_by(id=id).first()
    category.name = name
    db.session.commit()
    return redirect('category')
    # categories = Category.query.all()
    # return render_template('admin/category.html', categories=categories, current_user=current_user)

@csrf.exempt
@admin_blueprints.route("/delete_category", methods=["POST"])
@login_required
def delete_category():
    data = json.loads(request.form.get('data'))
    id = int(data['id'])
    print(id)
    Category.query.filter(Category.id == id).delete()
    db.session.commit()

    return redirect('category')

@csrf.exempt
@admin_blueprints.route("/add_category", methods=["POST"])
@login_required
def add_category():
    data = request.form['category']
    categories = Category.query.all()
    # 判断是否为空
    if data is None or data == "":
        return render_template('admin/category.html',categories=categories, current_user=current_user,msg="输入为空")
    # 判断是否存在
    for category in categories:
        if data == category.name:
            return render_template('admin/category.html', categories=categories, current_user=current_user,
                                   msg="类别已存在")
    category = Category(name=data, number=0)
    db.session.add(category)
    db.session.commit()
    return redirect('category')