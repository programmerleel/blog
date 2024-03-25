# -*- coding: utf-8 -*-
# @Time    : 2024/03/20 14:50
# @Author  : LiShiHao
# @FileName: forms.py
# @Software: PyCharm

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectMultipleField
from wtforms.validators import DataRequired, Length

# 登陆表单
class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), Length(1, 128)])
    remember = BooleanField('记住我！')
    submit = SubmitField('登录')


class BlogForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), Length(1, 40)])
    category = SelectMultipleField(
        label='类别', choices=[('Military', '军事'), ('New', '新闻'), ('Society', '社会'), ('Technology', '科技')])
    submit = SubmitField('发布')