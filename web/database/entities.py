from web import db

mailtags = db.Table('mailtags',
                    db.Column('mail_id', db.Integer, db.ForeignKey('mail.message_id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
)


class Mail(db.Model):
    message_id = db.Column(db.Integer, primary_key=True)
    in_reply_to = db.Column(db.Integer, db.ForeignKey('mail.message_id'))
    sender = db.Column(db.Text)
    subject = db.Column(db.Text)
    body = db.Column(db.Text)
    date = db.Column(db.DATETIME)
    tags = db.relationship('Tag', secondary=mailtags,
                           backref=db.backref('mails', lazy='dynamic'))

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


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.NVARCHAR(100), nullable=False)

    def __repr__(self):
        return '<Tag %r>' % self.name
