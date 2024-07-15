#!/usr/bin/python3
""" Index view
"""
from flask import jsonify, Blueprint

app_views = Blueprint('status', __name__)
@app_views.route('/status', methods=['GET'])
def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
