from app import app
from Models import db

with app.app_context():
    db.create_all()
