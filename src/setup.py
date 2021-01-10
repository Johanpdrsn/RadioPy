from app import app
from Models import db

# Create tables in db
with app.app_context():
    db.create_all()
