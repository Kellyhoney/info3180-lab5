# Add any model classes for Flask-SQLAlchemy here 
# models.py
# app/models.py

from . import db
from datetime import datetime

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    poster = db.Column(db.String(255))  # stores filename
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
