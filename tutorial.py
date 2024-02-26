from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

# Create a Flask app
app = Flask(__name__)

# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://beyza:labris@localhost/first_flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create a SQLAlchemy instance
db = SQLAlchemy(app)

app.permanent_session_lifetime = timedelta(days=30)


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


# Create the tables
db.create_all()


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


@app.route("/logout")
def logout():
    session.pop("user", None)
    session.pop("email", None)
    flash("You have been logged out!", "success")
    return redirect(url_for("login"))


@app.route("/user", methods=["POST", "GET"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user_base.html", user=user)
    else:
        flash("You are not logged in!", "info")
        return redirect(url_for("login"))


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
