from app import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    city = db.Column(db.String(60), nullable=False)
    zipcode = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f"User({self.username} - {self.email})"