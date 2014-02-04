import datetime
from flask import Blueprint, request, jsonify
from web import db
from web.database.entities import Mail
from web.emails.mailmod import fetch_emails, parse_emails

mod = Blueprint('synchronisation', __name__)


def hashify(s):
    return abs(hash(s)) % (10 ** 8)


@mod.route('/api/synchronise', methods=["POST"])
def synchronise():
    since = datetime.datetime.strptime(request.form["since"], "%Y-%m-%d")
    mails = fetch_emails(since)
    parsed = parse_emails(mails)
    for mail in parsed:
        mail_entity = Mail()
        mail_entity.body = mail['Body']
        mail_entity.subject = mail['Subject']
        mail_entity.message_id = hashify(mail['MessageId'])
        mail_entity.sender = mail['From']
        mail_entity.date = mail['Date']
        if mail['InReplyTo'] is not None:
            mail_entity.in_reply_to = hashify(mail['InReplyTo'])
        db.session.add(mail_entity)
    db.session.commit()
    return jsonify(success=True)

