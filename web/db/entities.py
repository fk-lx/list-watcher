from web import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    openid = db.Column(db.string(100))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    def __repr__(self):
        return '<User %r>' % self.name


class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Text)
    header = db.Column(db.Text)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)

    def __repr__(self):
        return '<Mail %r>' % self.subject

