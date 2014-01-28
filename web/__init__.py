from flask import Flask


app = Flask(__name__)
app.secret_key = 'why would I tell you my secret key?'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////db/listwatcher.db'

from flask.ext.openid import OpenID

oid = OpenID(app, 'storage/openid', safe_roots=[])

from web.views import general

app.register_blueprint(general.mod)


