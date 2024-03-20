# -*- coding: utf-8 -*-
# @Time    : 2024/03/20 14:03
# @Author  : LiShiHao
# @FileName: models.py
# @Software: PyCharm

from app.extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


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