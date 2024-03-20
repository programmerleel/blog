# -*- coding: utf-8 -*-
# @Time    : 2024/03/20 11:41
# @Author  : LiShiHao
# @FileName: __init__.py
# @Software: PyCharm

import os
from app.extensions import db, login_manager, csrf, mail,debug_tool
from app.views.admin import admin_blueprints
from app.views.auth import auth_blueprints
from flask import Flask

from app.views.blog import blog_blueprints


def create_app():
    base_dir = os.path.abspath(os.path.basename(__name__))
    app = Flask("blog",template_folder="./app/templates",static_folder="./app/static")
    app.config.from_pyfile(os.path.join(base_dir,"config.py"))

    # register_logging(app)
    register_extensions(app)
    register_blueprints(app)
    # register_commands(app)
    # register_errors(app)
    # register_shell_context(app)
    # register_template_context(app)
    # register_request_handlers(app)
    return app

def register_extensions(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
    login_manager.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    debug_tool.init_app(app)


def register_blueprints(app):
    app.register_blueprint(auth_blueprints, url_prefix='/auth')
    app.register_blueprint(admin_blueprints, url_prefix='/admin')
    app.register_blueprint(blog_blueprints, url_prefix='/blog')