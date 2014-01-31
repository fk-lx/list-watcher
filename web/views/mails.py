from flask import Blueprint, jsonify, json
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import joinedload, subqueryload
from web import db
from web.database.entities import Mail

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

@mod.route('/api/getmails', methods=['GET'])
def get_mails():
    mails = db.session.query(Mail).options(subqueryload(Mail.mails)).filter(Mail.in_reply_to == None).all()
    return json.dumps(mails, cls=AlchemyEncoder)
