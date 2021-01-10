from src.app import app
from src.Models import db

with app.app_context():
    db.create_all()
