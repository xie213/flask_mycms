# -- * -- coding : utf-8 -- * --
# 第三方

from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap
from flask_mail import Mail



bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()
# 实例化第三方插件
def config_extension(app):
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)
    # 蓝图
    from App.user.views import user
    app.register_blueprint(user,url_prefix='')
