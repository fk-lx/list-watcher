from flask import render_template, Blueprint, g, session, flash, redirect, url_for, request
from flask.ext.login import login_user
from web import oid, db, lm
from web.database.entities import User

mod = Blueprint('general', __name__)


@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    if request.method == 'POST':
        openid = request.form.get('openid')
        if openid:
            return oid.try_login(openid, ask_for=['email', 'nickname'],
                                 ask_for_optional=['fullname'])
    return render_template('login.html', next=oid.get_next_url(),
                           error=oid.fetch_error())


@mod.route('/logout')
def logout():
    session.pop('openid', None)
    flash(u'You were signed out')
    return redirect(oid.get_next_url())


@mod.before_app_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        openid = session['openid']
        user = db.session.query(User).filter(User.openid == openid).first()
        g.user = user


@oid.after_login
def create_or_login(resp):
    user = db.session.query(User).filter(User.email == resp.email).first()
    if user is not None:
        flash(u'Successfully signed in')
        session['openid'] = resp.identity_url
        g.user = user
        login_user(user)
        return redirect(oid.get_next_url())
    flash(u'You are not authenticated.')
    return redirect(oid.get_next_url())

@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))
