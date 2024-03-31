# -*- coding: utf-8 -*-
# @Time    : 2024/03/20 14:03
# @Author  : LiShiHao
# @FileName: models.py
# @Software: PyCharm

from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# 管理员类
class Admin(db.Model, UserMixin):
    id = db.Column(db.Integer, nullable=False,primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    # 不使用明文保存密码
    password_hash = db.Column(db.String(128),nullable=False)
    # 用于回复时名字
    name = db.Column(db.String(20),nullable=False)

    # 生成密码hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # 验证密码hash
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

#博客类 按照类别标题 方便进行检索 内容以html形式保存
class Blog(db.Model):
    id = db.Column(db.Integer,nullable=False,primary_key=True,autoincrement=True)
    title = db.Column(db.String(40),nullable=False)
    date = db.Column(db.Date, nullable=False)
    # 外键 绑定种类
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'),nullable=False)
    # 外键 绑定评论
    comment_id = db.Column(db.Integer,db.ForeignKey('comment.id'),nullable=False)

#类别类
class Category(db.Model):
    id = db.Column(db.INTEGER, nullable=False,primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    number = db.Column(db.INTEGER, nullable=False)

#回复类
class Reply(db.Model):
    id = db.Column(db.INTEGER, nullable=False,primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40),nullable=False)
    body = db.Column(db.String(512),nullable=False)
    date = db.Column(db.Date,nullable=False)

#评论类
class Comment(db.Model):
    id = db.Column(db.INTEGER, nullable=False,primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40),nullable=False)
    body = db.Column(db.String(512),nullable=False)
    date = db.Column(db.Date,nullable=False)
    blog_id = db.Column(db.Integer,db.ForeignKey('blog.id'),nullable=False)
    reply_id = db.Column(db.Integer,db.ForeignKey('reply.id'),nullable=False)

