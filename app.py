# import os
# from flask import Flask, render_template, request, url_for, redirect
# from flask_restful import Api, Resource
# from flask_migrate import Migrate
# from werkzeug.security import generate_password_hash

# from models import db, User
# from flask import jsonify
# from datetime import datetime
#
# from sqlalchemy.sql import func


# app = Flask(__name__)
# api = Api(app)

# # Configure SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://beyza:labris@localhost/flask_db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance and handle database migrations

# migrate = Migrate(app, db)
# db.init_app(app)


# @app.route('/')
# def home():
#     print("Home page!")
#     return render_template('user_base.html')
#
#
# @app.route('/user/list')
# def user_list():
#     users = User.query.all()
#     return render_template('user_list.html', users=users)
#
#
# @app.route('/user/create', methods=('GET', 'POST'))
# def user_create():
#     if request.method == 'POST':
#         # Get the data from the request body
#         username = request.form['username']
#         firstname = request.form['firstname']
#         middlename = request.form['middlename']
#         lastname = request.form['lastname']
#         birthdate = request.form['birthdate']
#         email = request.form['email']
#         password = request.form['password']
#
#         # Create a new user instance
#         new_user = User(username=username, firstname=firstname, middlename=middlename, lastname=lastname,
#                         birthdate=birthdate, email=email, password=generate_password_hash(password, method='sha256'))
#
#         db.session.add(new_user)
#         db.session.commit()
#
#         return redirect(url_for('user_list'))
#
#     return render_template('user_create.html')
#
#
# @app.route('/user/update/<int:id>', methods=('GET', 'POST'))
# def user_update(id):
#     user = User.query.get_or_404(id)
#
#     if request.method == 'POST':
#         username = request.form['username']
#         firstname = request.form['firstname']
#         middlename = request.form['middlename']
#         lastname = request.form['lastname']
#         birthdate = request.form['birthdate']
#         email = request.form['email']
#
#         user.username = username
#         user.firstname = firstname
#         user.middlename = middlename
#         user.lastname = lastname
#         user.birthdate = birthdate
#         user.email = email
#
#         db.session.add(user)
#         db.session.commit()
#
#         return redirect(url_for('user_list'))
#
#     return render_template('user_update.html', user=user)
#
#
# @app.post('/user/delete/<int:id>')
# def user_delete(id):
#     user = User.query.get_or_404(id)
#     db.session.delete(user)
#     db.session.commit()
#     return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
