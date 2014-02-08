from flask import Blueprint, render_template, redirect, url_for, jsonify, request, json
from flask.ext.login import login_required
from web import db
from web.database.entities import Tag
from web.views.mails import AlchemyEncoder

mod = Blueprint('tags', __name__)

@login_required
@mod.route('/tags/', methods=['GET'])
def view_tags():
    tags = db.session.query(Tag).all()
    return render_template('tags.html', tags=tags)

@login_required
@mod.route('/tags/add', methods=['POST'])
def add_tag():
    req_json = request.get_json()
    name = req_json['name']
    tag = Tag()
    tag.name = name
    db.session.add(tag)
    db.session.commit()
    return jsonify(id=tag.id)

@login_required
@mod.route('/tags/edit/', methods=['POST'])
def edit_tag():
    rq_form = request.form
    tag_id = rq_form['id']
    name = rq_form['value']
    tag = db.session.query(Tag).filter(Tag.id == tag_id).first()
    tag.name = name
    db.session.commit()
    return name

@login_required
@mod.route('/tags/delete', methods=['DELETE'])
def delete_tag():
    req_json = request.get_json()
    tag_id = req_json['id']
    db.session.query(Tag).filter(Tag.id == tag_id).delete()
    db.session.commit()
    return jsonify(success=True)


@mod.route('/tags/all')
def get_all_tags():
    tags = db.session.query(Tag).all()
    return json.dumps(tags, cls=AlchemyEncoder)