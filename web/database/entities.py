from web import db


class Mail(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    in_reply_to = db.Column(db.Integer, db.ForeignKey('mail.message_id'))
    sender = db.Column(db.Text)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)
    mails = db.relationship('Mail', lazy="joined", join_depth=2)
    def __repr__(self):
        return '<Mail %r>' % self.mails

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    openid = db.Column(db.String(100))

    def __init__(self, name, openid):
        self.name = name
        self.openid = openid

    def __repr__(self):
        return '<User %r>' % self.name