from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, DB_Manager
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=('GET', 'POST'))
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    manager = DB_Manager.query.filter_by(email=email).first()
    if manager:
        if check_password_hash(manager.password, password):
            flash('Logged in successfully!', category='success')
            return redirect(url_for('main.home'))
        else:
            flash('Incorrect password, try again.', category='error')
    else:
        flash('Email does not exist.', category='error')
        return redirect(url_for('auth.login'))


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    # validate and add user
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    # check if email has been used before
    manager = DB_Manager.query.filter_by(email=email).first()

    # if a user is found, we want to redirect back to signup page so user can try again
    if manager:
        flash('Email address already exists.')
        return redirect(url_for('auth.signup'))

    # create a new manager with the form data. Hash the password so the plaintext version isn't saved.
    new_manager = DB_Manager(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new manager to the database
    db.session.add(new_manager)
    db.session.commit()

    flash('The account created successfully.')
    return redirect(url_for('auth.login'))


# @auth.route('/logout')
# def logout():
#     return 'Logout'