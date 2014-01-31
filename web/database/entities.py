from web import db


class Mail(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Text)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)
    #in_reply_to = db.Column(db.Text, nullable=True)
    message_id = db.Column(db.Integer, primary_key=True)
    in_reply_to = db.Column(db.Integer, db.ForeignKey(message_id))
    #mail_id = db.Column(db.Text, db.ForeignKey(message_id))
    #mail_id = db.Column(db.Integer, db.ForeignKey(id))
    mails = db.relationship('Mail', remote_side=[message_id])
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