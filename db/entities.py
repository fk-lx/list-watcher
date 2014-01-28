from flask.ext.sqlalchemy import SQLAlchemy
from web.views.general import app

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    openid = db.Column(db.string(100))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid