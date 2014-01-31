import os

basedir = os.path.abspath(os.path.dirname(__file__))

secret_key = 'extremely secret key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database/app.db')