# -*- coding: utf-8 -*-
# @Time    : 2024/03/20 14:03
# @Author  : LiShiHao
# @FileName: extensions.py
# @Software: PyCharm

"""
注册插件
"""

import datetime
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

# debug工具
debug_tool = DebugToolbarExtension()
# 登陆管理
login_manager = LoginManager()
# 邮件
mail = Mail()
# 数据库orm
db = SQLAlchemy()
# csrf保护
csrf = CSRFProtect()

# 用于login_required回调 检查与session中的id是否对应
@login_manager.user_loader
def load_user(id):
    # 避免循环引用报错
    from app.models import Admin
    user = Admin.query.get(int(id))
    return user

# 绑定视图
login_manager.login_view = "auth.login"
# 设置消息类别
login_manager.login_message_category = "warning"
# 会话保护强度
login_manager.session_protection = "strong"
# remember cookie保存时间
login_manager.remember_cookie_duration = datetime.timedelta(days=14)
# 设置cookie不能从客户端脚本访问
login_manager.remember_cookie_httponly = True
