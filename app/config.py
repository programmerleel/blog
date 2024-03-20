# -*- coding: utf-8 -*-
# @Time    : 2024/03/19 17:16
# @Author  : LiShiHao
# @FileName: config.py
# @Software: PyCharm

import os

base_dir = os.path.abspath(os.path.basename(__name__))

SECRET_KEY='Lee Blog'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, '../data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False