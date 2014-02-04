from web import db


class Mail(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    in_reply_to = db.Column(db.Integer, db.ForeignKey('mail.message_id'))
    sender = db.Column(db.Text)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)
    date = db.Column(db.DATETIME)
    remarks = db.Column(db.Text, nullable=True)
    def __repr__(self):
        return '<Mail %r>' % self.mails


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.NVARCHAR(100), nullable=False)
    openid = db.Column(db.NVARCHAR(100), nullable=True)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '%r' % self.email