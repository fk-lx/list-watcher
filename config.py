import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'extremely secret key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/app.db')

#configuration for mail fetching
MAIL_HOST = 'imap.gmail.com'
MAIL_PORT = '993'
MAIL_LOGIN = 'opensource.mer@gmail.com'
MAIL_PASSWORD = ''
MAIL_FILTER = 'mer'