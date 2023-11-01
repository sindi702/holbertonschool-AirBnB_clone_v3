#!/usr/bin/python3
"""First route to display a JSON object"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

tables = {
    "amenities": Amenity,
    "cities": City,
    "places": Place,
    "reviews": Review,
    "states": State,
    "users": User
}

@app_views.route('/status')
def status():
    """Status route to return a JSON object"""
    return jsonify(status="OK")

@app_views.route('/status')
def stats():
    """Statistics route to return counts of objects"""
    counts = {}
    for key, val in tables.items():
        counts[key] = storage.count(val)
    return jsonify(**counts)

