from flask import Flask

from App.config import envs
from App.extension import config_extension
from App.user.views import Blueprint

def create_app(config_name):
    #app 实例化
    app = Flask(__name__)

    app.config.from_object(envs.get(config_name))
    envs[config_name].init_app(app)
    # 实例化第三方
    config_extension(app)

    return app