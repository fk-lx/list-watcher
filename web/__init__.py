from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from flask.ext.openid import OpenID

oid = OpenID(app, 'storage/openid', safe_roots=[])

from web.views import general

app.register_blueprint(general.mod)

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)