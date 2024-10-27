# server/models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)  
    genre = db.Column(db.String, nullable=True)   
    release_year = db.Column(db.Integer, nullable=True)  

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "genre": self.genre,
            "release_year": self.release_year,
        }

class Message(db.Model):
    __tablename__ = 'messages'

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)

    def to_dict(self):
        """Convert model instance to dictionary."""
        return {
            "id": self.id,
            "body": self.body,
        }
