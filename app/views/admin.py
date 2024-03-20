# -*- coding: utf-8 -*-
# @Time    : 2024/3/20 22:27
# @Author  : Lee
# @Project ：blog-master 
# @File    : admin.py

# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 15:40
# @Author  : LiShiHao
# @FileName: auth.py.py
# @Software: PyCharm

from flask import Blueprint, render_template
from flask_login import login_required

# 注册蓝图
admin_blueprints = Blueprint("admin", __name__)

@admin_blueprints.route("/index", methods=["GET","POST"])
@login_required
def login():
    # 跳转管理界面
    return render_template('admin/index.html')
