# -*- coding: utf-8 -*-
"""
@author 仔仔
@date 2024-03-16 23:51:51
@describe TODO
"""
import flask
from flask import Blueprint

blueprint = Blueprint('student', __name__, url_prefix='/student')


@blueprint.route('/detail')
def detail():
    data = {'id': 123, 'name': '仔仔'}
    return flask.make_response(data, 400)
