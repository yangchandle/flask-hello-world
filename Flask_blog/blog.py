# !/user/bin/env python
# blog.py - controller

# imports
from flask import Flask, render_template, request, session, flash, redirect, url_for, g

import sqlite3

from functools import wraps

# configuration
DATABASE = 'blog.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'hard_to_guess'

app = Flask(__name__)

# pulls in app configuration by looking for UPPERCASE varibles
app.config.from_object(__name__)




# function used for connecting to the database
def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


def login_required(test):
	@wraps(test)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return test(*args, **kwargs)
		else:
			flash('You need to log in first.')
			return redirect(url_for('login'))
	return wrap

@app.route("/", methods=['GET', 'POST'])
def login():
	error = None
	status_code = 200
	if request.method == 'POST':
		if request.form['username'] != app.config['USERNAME'] or \
			request.form['password'] != app.config['PASSWORD']:
			error = 'Invalid Credentials. Please try agian.'
			status_code = 401
		else:
			session['logged_in'] = True
			return redirect(url_for('main'))
	return render_template('login.html', error=error), status_code
	

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You were logged out')
	return redirect(url_for('login'))

@app.route("/main")
@login_required
def main():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	posts = [dict(title=row[0], post=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template('main.html', posts=posts)

if __name__ == '__main__':
	app.run(debug=True)