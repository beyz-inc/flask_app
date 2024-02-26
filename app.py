from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
CORS(app)
# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:labris@localhost:5432/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

# Create a SQLAlchemy instance
api = Api(app)


@app.route("/")  # this sets the route to this page
def home():
    return redirect(url_for("login"))


@app.route("/login", methods=["POST", "GET"])
def login():  # return "This is the login page. <h1>HELLO, AFTER YOU</h1>"
    email = None
    if request.method == "POST":
        session.permanent = True
        user = request.form["username"]
        session["user"] = user
        email = request.form["email"]
        session["email"] = email
        #
        # found_user = User.query.first()
        # if:
        #
        # else:
        #     user = User(user, "")
        #     db.session.add(user)
        #     db.session.commit()


        flash("Login successful!", "success")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already logged in!", "info")
            return redirect(url_for("user"))
    return render_template("login.html")


class UserCreate(Resource):
    # /user/create
    def post(self):
        # Get the data from the request body
        data = request.get_json()
        username = data.get('username')
        firstname = data.get('firstname')
        middlename = data.get('middlename')
        lastname = data.get('lastname')
        birthdate = data.get('birthdate')
        email = data.get('email')
        password = data.get('password')

        # Create a new user instance
        new_user = User(username=username, firstname=firstname, middlename=middlename, lastname=lastname, birthdate=birthdate, email=email, password=password)

        # Add the new user to the session and commit changes to the database
        db.session.add(new_user)
        db.session.commit()

        flash("User created successfully", "success")

        return render_template("user_create.html")


class UserList(Resource):
    # /user/list
    def get(self):
        users = User.query.all()
        return {'users': [user.to_dict() for user in users]}, 200


# class Login(Resource):
#     def get(self):
#     def post(self):
#
# class Logout(Resource):
#     def get(self):
#     def post(self):
#

#
#
#
# class UserDelete(Resource):
#     # /user/delete/{id}
#     def delete(self, id):
#         user = User.query.get(id)
#         if not user:
#             return {'error': 'User not found'}, 404
#         db.session.delete(user)
#         db.session.commit()
#         return {'message': 'User deleted successfully'}, 200
#
# class UserUpdate(Resource):
#     # /user/update/{id}
#     def put(self, id):
#         user = User.query.get(id)
#         if not user:
#             return {'error': 'User not found'}, 404
#         data = request.get_json()
#         username = data.get('username')
#         firstname = data.get('firstname')
#         middlename = data.get('middlename')
#         lastname = data.get('lastname')
#         birthdate = data.get('birthdate')
#         email = data.get('email')
#         password = data.get('password')
#
#         username = data.get('username')
#         if username is not None:
#             user.username = username
#
#
#
#         user.username = username
#         user.password = password
#         db.session.commit()
#         return {'message': 'User updated successfully'}, 200
#
# class OnlineUsers(Resource):
#     def get(self):


# Add the resource to the API
api.add_resource(UserCreate, '/user/create')
api.add_resource(UserList, '/user/list')


# api.add_resource(UserList, '/user/list')
# api.add_resource(UserDelete, '/user/delete/{id}')
# api.add_resource(UserUpdate, '/user/update/{id}')


if __name__ == "__main__":
    app.run(port=5555, debug=True)