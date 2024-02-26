# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            'username': self.username,
            'firstname': self.firstname,
            'middlename': self.middlename,
            'lastname': self.lastname,
            'birthdate': self.birthdate,
            'email': self.email,
            'password': self.password
        }