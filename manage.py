from flask_migrate import MigrateCommand,Migrate
from flask_script import Manager
from App import create_app
import os

from App.extension import db
from App.user.models import User

# 导入App配置     os.environ的意思就是从系统环境变量
app = create_app(os.environ.get('FLASK_CONFIG')or 'default')
# 命令行
manager = Manager(app)
# 数据库迁移
Migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    manager.run()
