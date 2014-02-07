from flask import Blueprint, jsonify, json, request, render_template
from flask.ext.login import login_required
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import joinedload, subqueryload
from web import db
from web.database.entities import Mail
from web.database.entities import Tag

mod = Blueprint('mails', __name__)

class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return json.JSONEncoder.default(self, obj)

@mod.route('/mails/', methods=['GET'], defaults={'ident': None})
@mod.route('/mails/<ident>', methods=['GET'])
def get_mails(ident):
    mail = db.session.query(Mail).filter(Mail.message_id == ident).first()
    mails = db.session.query(Mail).filter(Mail.in_reply_to == ident).order_by(Mail.date.desc()).all()
    tags = mail.tags if mail is not None else None
    return render_template('mails.html', mails=mails, mail=mail, tags=tags)

@login_required
@mod.route('/mails/addtag/', methods=['POST'])
def add_mail_tags():
    tags = request.form.getlist("tags")
    mail_id = request.referrer.split('/')[-1]
    mail = db.session.query(Mail).filter(Mail.message_id == mail_id).first()
    for t in mail.tags[:]:
        mail.tags.remove(t)
    for tag in tags:
        tag = db.session.query(Tag).filter(Tag.name == tag).first()
        mail.tags.append(tag)
    db.session.commit();
    return jsonify(success=True)

@mod.route('/mails/tags/<mail_id>', methods=['GET'])
def get_tags(mail_id):
    mail = db.session.query(Mail).filter(Mail.message_id == mail_id).first()
    return json.dumps(mail.tags, cls=AlchemyEncoder)

