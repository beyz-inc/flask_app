from flask import render_template, request, url_for, redirect, Blueprint
from . import db
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    print("Home page!")
    return render_template('user_base.html')


@main.route('/user/list')
def user_list():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@main.route('/user/create', methods=('GET', 'POST'))
def user_create():
    if request.method == 'POST':
        # Get the data from the request body
        username = request.form['username']
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        birthdate = request.form['birthdate']
        email = request.form['email']
        password = request.form['password']

        # Create a new user instance
        new_user = User(username=username, firstname=firstname, middlename=middlename, lastname=lastname,
                        birthdate=birthdate, email=email, password=generate_password_hash(password, method='sha256'))



        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('user_list'))

    return render_template('user_create.html')


@main.route('/user/update/<int:id>', methods=('GET', 'POST'))
def user_update(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        username = request.form['username']
        firstname = request.form['firstname']
        middlename = request.form['middlename']
        lastname = request.form['lastname']
        birthdate = request.form['birthdate']
        email = request.form['email']

        user.username = username
        user.firstname = firstname
        user.middlename = middlename
        user.lastname = lastname
        user.birthdate = birthdate
        user.email = email

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('user_list'))

    return render_template('user_update.html', user=user)


@main.post('/user/delete/<int:id>')
def user_delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('home'))