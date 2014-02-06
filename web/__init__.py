from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
app.config.from_object('config')
app.wsgi_app = ProxyFix(app.wsgi_app)

from flask.ext.openid import OpenID

oid = OpenID(app, 'storage/openid', safe_roots=[])

from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

from flask.ext.login import LoginManager

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'general.login'

from web.views import general, synchronisation, mails, tags

app.register_blueprint(general.mod)
app.register_blueprint(synchronisation.mod)
app.register_blueprint(mails.mod)
app.register_blueprint(tags.mod)

