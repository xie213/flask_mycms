#!/usr/bin/env python
# encoding: utf-8
def get_db_uri(dbinfo):

    engine = dbinfo.get("ENGINE")
    driver = dbinfo.get("DRIVER")
    user = dbinfo.get("USER")
    password = dbinfo.get("PASSWORD")
    host = dbinfo.get("HOST")
    port = dbinfo.get("PORT")
    name = dbinfo.get("NAME")

    return "{}+{}://{}:{}@{}:{}/{}".format(engine, driver,user, password, host, port, name)


class Config:

    DEBUG = False

    TESTING = False

    SECRET_KEY = "wertyuiodfghjkl!@#$%^&I(*&^5"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 邮件配置
    # 服务器ip地址
    MAIL_SERVER = "smtp.qq.com"
    # 端口号:TLS对应587,SSL对应465
    MAIL_PORT = "587"
    MAIL_USE_TLS = True
    # MAIL_USE_SSL : 默认为 False
    # 默认发送者
    MAIL_DEFAULT_SENDER = "dalongmao.zhang@qq.com"

    # 发送者邮箱
    MAIL_USERNAME = "dalongmao.zhang@qq.com"
    MAIL_PASSWORD = "ohhvvhwltfovbgac"

    # 注册token激活有效期
    EXPIRES_IN_TOKEN = 3600

    @staticmethod
    def init_app(app):
        pass

class DevelopConfig(Config):

    DEBUG = True

    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "oo"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)




class TestingConfig(Config):

    TESTING = True


class StagingConfig(Config):

    pass


class ProductConfig(Config):

    pass


envs = {
    #生产环境
    "develop": DevelopConfig,
    #测试环境
    "testing": TestingConfig,
    # 演示
    "staging": StagingConfig,
    #线上
    "product": ProductConfig,
    #默认 生产
    "default": DevelopConfig,
}
