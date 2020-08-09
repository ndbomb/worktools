"""
初始化app,注册扩展

"""
from flask import Flask
from .views import register_bp
from .settings import default_setting
from .expension import register_expension



def create_app():
    app = Flask(__name__)
    register_expension(app)
    default_setting(app)
    register_bp(app)
    
    return app
