from flask import render_template, Blueprint, g, session, flash, redirect, url_for, request
from web import oid

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


@mod.before_request
def lookup_current_user():
    g.user = None
    if 'openid' in session:
        openid = session['openid']
        g.user = openid


@oid.after_login
def create_or_login(resp):
    session['openid'] = resp.identity_url
    user = resp.identity_url
    if user is not None:
        flash(u'Successfully signed in')
        g.user = user
        return redirect(oid.get_next_url())
    return redirect(url_for('create_profile', next=oid.get_next_url(), name=resp.fullname or resp.nickname),
                    email=resp.email)
