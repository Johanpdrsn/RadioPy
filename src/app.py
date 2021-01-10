from flask.wrappers import Response
from Models import Device, Location
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from Models import Device


# Initialize Flask app with SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


@app.route('/radios/<id>', methods=['POST'])
def create_device(id) -> Response:
    if not request.is_json or 'alias' not in request.get_json() or "allowed_locations" not in request.get_json():
        return Response(status=400)

    device = Device(id, request.get_json()["alias"])
    for loc in request.get_json()["allowed_locations"]:
        location = Location(loc, device.id)
        db.session.add(location)

    db.session.add(device)

    db.session.commit()

    return jsonify(device.serialize), 201


@app.route('/radios/<id>/location', methods=["POST"])
def set_location(id) -> Response:
    device = Device.query.filter_by(id=id).first()

    if not device or "location" not in request.get_json():
        return Response(status=400)

    allowed_locations = [
        location.location for location in device.allowed_locations]

    if request.get_json()["location"] not in allowed_locations:
        return Response(status=403)

    device.location = request.get_json()["location"]
    db.session.commit()
    return Response(status=200)


@app.route('/radios/<id>/location', methods=["GET"])
def get_location(id) -> Response:
    device = Device.query.filter_by(id=id).first()
    if not device or device.location == None:
        return Response(status=404)
    return jsonify({"location": device.location}), 200
