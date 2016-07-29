# coding=utf-8
import random

import names
from flask import jsonify, make_response, request
from google.appengine.api import app_identity
from google.appengine.ext.ndb import Key, AND

from application import app
from models import *

__all__ = ['create_user',
           'update_user',
           'get_user']

SERVER_URL = app_identity.get_default_version_hostname()


def _to_dict(model):
    dic = model.to_dict()
    dic['id'] = model.key.id()

    return dic


def _make_rest_response(data, entity_id):
    resp = make_response(jsonify(data))
    resp.status_code = 201
    resp.headers['Location'] = '%s%s/%s' % (SERVER_URL,
                                            request.path,
                                            str(entity_id))

    return resp


@app.route('/api/user', methods=['POST'])
def create_user():
    user = User()
    user.name = names.get_full_name()
    user.username = '%s@email.com' % user.name.replace(" ", "_")
    user.put()

    dic = user.to_dict()
    dic['id'] = user.key.id()

    return _make_rest_response(dic, user.key.id())


@app.route('/api/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user_key = Key(User, user_id)
    user = user_key.get()

    lat = random.random() * 180 - 90
    lng = random.random() * 360 - 180

    if not user.location:
        user.location = Location()

    user.location.lat = lat
    user.location.lng = lng

    user.put()

    return jsonify(_to_dict(user))


@app.route('/api/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user_key = Key(User, user_id)
    user = user_key.get()

    if not user:
        return 'User not found!', 404

    return jsonify(_to_dict(user))


@app.route('/api/incident', methods=['POST'])
def create_incident():
    incident = Incident()
    incident.name = names.get_full_name()
    incident.username = '%s@email.com' % incident.name.replace(" ", "_")
    incident.put()

    dic = incident.to_dict()
    dic['id'] = incident.key.id()

    return _make_rest_response(dic, incident.key.id())


@app.route('/api/incident', methods=['GET'])
def find_incident():
    lat = request.args.get('lat', None)
    lng = request.args.get('lng', None)

    if lat and lng:
        q = Location.query(AND(Location.lat > 'lat',
                               Location.lng > 'lng'))

        locs = ''
        for e in q:
            locs += str(e) + '<br><br>'
            # e.key.delete()

        return '<HTML><HEAD></HEAD><BODY>%s</BODY></HTML' % str(locs)

@app.route('/api/user', methods=['GET'])
def find_incident():
    names = request.args.getlist('name')

    linfo(names)
    if names:
        q = User.query(User.name.IN(names))

        users = ''
        linfo(str(q.count()))
        for e in q:
            linfo(str(e))
            users += str(e) + '<br><br>'
            # e.key.delete()

        return '<HTML><HEAD></HEAD><BODY>%s</BODY></HTML' % users

    resp = make_response('')
    resp.status_code = 204
    return resp
