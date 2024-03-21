# -*- coding: utf-8 -*-
# @Time    : 2024/3/20 22:26
# @Author  : Lee
# @Project ：blog-master 
# @File    : blog.py
from flask_login import login_required, current_user

# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 15:40
# @Author  : LiShiHao
# @FileName: auth.py.py
# @Software: PyCharm

from flask import Blueprint, render_template

# 注册蓝图
blog_blueprints = Blueprint("blog", __name__)

@blog_blueprints.route("/index", methods=["GET","POST"])
@login_required
def index():
    # 跳转管理界面
    return render_template('blog/index.html')

