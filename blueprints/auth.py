# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 15:40
# @Author  : LiShiHao
# @FileName: auth.py.py
# @Software: PyCharm

from flask import Blueprint,render_template

auth_blueprints = Blueprint("auth",__name__)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String,nullable=False)

@auth_blueprints.route("/register",methods=["POST"])
def register():
    return render_template("auth/register.html")