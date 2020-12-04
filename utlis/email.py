# -- * -- coding : utf-8 -- * --
from  flask import current_app,render_template

from flask_mail import Message
from App.extension import mail
from threading import Thread

def async_send_email(app,msg):
    with app.app_context():
        mail.send(msg)


def send_email(to,subject,template,**kwargs):
    app = current_app._get_current_object()
    msg = Message(subject=subject,sender=app.config['MAIL_USERNAME'],recipients=[to])
    msg.html = render_template(template + '.html',**kwargs)
    # msg.body = render_template(template + '.txt',**kwargs)
    thr = Thread(target=async_send_email,args=[app,msg])
    thr.start()
    return thr