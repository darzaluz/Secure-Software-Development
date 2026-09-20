from flask import Flask, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

#-------------------
# CREATING DATABASE
#-------------------
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute ("""
CREATE TABLE IF NOT EXISTS users (
	id INTEGER PRIMARY KEY,
	username TEXT UNIQUE,
	password_hash TEXT
)
""")
#----------------------
#CREATING SAMPLE USERS
#----------------------

users = [
	("diego", "tennis123"),
	("maria", "soccer123"),
	("david", "basketball123"),
	("ale", "softball123")
]

for username, plain_password in users:

	password_hash = generate_password_hash(plain_password)

	cursor.execute(
		"INSERT OR IGNORE INTO users (username, password_hash) VALUES (?,?)",
		(username, password_hash)
)

connection.commit()
connection.close()

#------------------
#LOGIN WEBSITE
#------------------

@app.route("/")
def home ():
	return """
	<h2>Secure Login</h2>

	<form method="post" action="/login">

		<label>Username:</label>
		<input type="text" name="username">
	
		<br><br>

		<label>Password:</label>
		<input type="password" name="password">

		<br><br>

		<button type="submit">Login</button>

</form>
"""

#----------------------
#LOGIN PROCESS
#----------------------
@app.route("/login", methods=["POST"])
def login():

	username = request.form["username"]
	password = request.form["password"]

	connection = sqlite3.connect("users.db")
	cursor = connection.cursor()

	cursor.execute(
		"SELECT password_hash FROM users WHERE username = ?",
		(username,)
	)

	user = cursor.fetchone()

	connection.close()

	if user and check_password_hash(user[0],password):
		return "Log in succesful"

	return "Invalid username or password"

#-------------------------
#RUN WEBSITE WITH HTTPS
#-------------------------

if __name__ == "__main__":
	app.run(host="0.0.0.0", ssl_context="adhoc")
