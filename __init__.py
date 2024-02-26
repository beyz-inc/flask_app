from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
        host="localhost",
        database="deneme",
        user="beyza",
        password="labris")


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello, World!'


@app.route('/create', methods=['GET', 'POST'])
def create():
    # Get the username and email from the request body
    username = request.form.get('username')
    email = request.form.get('email')

    # Insert the data into the database
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXIST users (id SERIAL PRIMARY KEY, username VARCHAR(255), email VARCHAR(255));"
    )
    cur.execute(
        "INSERT INTO users (username, email) VALUES (%s, %s)", (username, email))
    conn.commit()

    cur.close()
    conn.close()
    return 'User created successfully!'


if __name__ == '__main__':
    app.run(debug=True)

# # Open a cursor to perform database operations
# cur = conn.cursor()
#
# # Execute a command: this creates a new table
# cur.execute('DROP TABLE IF EXISTS users;')
#
# conn.commit()
#
# cur.close()
# conn.close()