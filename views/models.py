from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    firstname = db.Column(db.String(50), nullable=False)
    middlename = db.Column(db.String(50), nullable=True)
    lastname = db.Column(db.String(50), nullable=False)
    birthdate = db.Column(db.DateTime, nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, username, firstname, middlename, lastname, birthdate, email, password):
        self.username = username
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'firstname': self.firstname,
            'middlename': self.middlename,
            'lastname': self.lastname,
            'birthdate': self.birthdate.isoformat(),  # Convert to ISO format for better serialization
            'email': self.email,
            'password': self.password  # Note: Be cautious about exposing passwords
        }