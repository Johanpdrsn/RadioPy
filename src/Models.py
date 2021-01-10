from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class Device(db.Model):
    '''Class modelling the radio device'''
    id = db.Column(db.Integer(), primary_key=True)
    alias = db.Column(db.String(), nullable=False)
    location = db.Column(db.String())
    allowed_locations = db.relationship(
        "Location", backref="device", lazy="select")

    def __init__(self, id, alias) -> None:
        super().__init__()
        self.location = None
        self.id = id
        self.alias = alias

    @property
    def serialize(self):
        """Method that allows serialization of the Device object"""
        return {
            'id': self.id,
            'alias': self.alias,
            'location': self.location,
            'allowed_locations': [location.location for location in self.allowed_locations]
        }


class Location(db.Model):
    '''Class modelling a location'''
    id = db.Column(db.Integer(), primary_key=True)
    location = db.Column(db.String(), nullable=False)
    device_id = db.Column(db.Integer, db.ForeignKey(
        'device.id'), nullable=False)

    def __init__(self, location, device_id) -> None:
        super().__init__()
        self.location = location
        self.device_id = device_id

    @property
    def serialize(self) -> None:
        """Method that allows serialization of the Location object"""
        return {
            'id': self.id,
            'device_id': self.device_id,
            'location': self.location,
        }
