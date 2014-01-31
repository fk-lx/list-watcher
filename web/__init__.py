from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask.ext.openid import OpenID

oid = OpenID(app, 'storage/openid', safe_roots=[])

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from web.views import general, synchronisation, mails

app.register_blueprint(general.mod)
app.register_blueprint(synchronisation.mod)
app.register_blueprint(mails.mod)
