from flask.wrappers import Response
from Models import Device
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from Models import Device


# Initialize Flask app with SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)


# Route for adding device by id
@app.route('/radios/<id>', methods=['POST'])
def create_device(id) -> Response:
    # Check for correct payload
    if not request.is_json or 'alias' not in request.get_json() or "allowed_locations" not in request.get_json():
        return Response(status=400)

    # Ids are unique
    if Device.query.filter_by(id=id).first():
        return Response("Device already exists", status=409)

    # Add device and location to database
    device = Device(id, request.get_json()[
                    "alias"], request.get_json()["allowed_locations"])

    db.session.add(device)
    db.session.commit()

    return jsonify(device.serialize), 201

# Set location of device with <id>


@app.route('/radios/<id>/location', methods=["POST"])
def set_location(id) -> Response:
    device = Device.query.filter_by(id=id).first()

    # Check for correct payload
    if not device or "location" not in request.get_json():
        return Response(status=400)

    allowed_locations = [
        location.location for location in device.allowed_locations]

    # Ensure location is allowed
    if request.get_json()["location"] not in allowed_locations:
        return Response(status=403)

    # Update the location
    db.session.query(Device).filter(Device.id == id).\
        update({Device.location: request.get_json()[
               "location"]}, synchronize_session=False)
    db.session.commit()

    return Response(status=200)

# Get the location of device with <id>


@app.route('/radios/<id>/location', methods=["GET"])
def get_location(id) -> Response:
    device = Device.query.filter_by(id=id).first()
    # Check that location is set
    if not device or device.location == None:
        return Response(status=404)
    return jsonify({"location": device.location}), 200
