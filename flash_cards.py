import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash

application = Flask(__name__)
application.config.from_object(__name__)

@application.route('/')
def index():
    if session.get('logged_in'):
        return redirect(url_for('general'))
    else:
        return redirect(url_for('login'))


@application.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != application.config['USERNAME']:
            error = 'Invalid username or password!'
        elif request.form['password'] != application.config['PASSWORD']:
            error = 'Invalid username or password!'
        else:
            session['logged_in'] = True
            session.permanent = True  # stay logged in
            return redirect(url_for('cards'))
    return render_template('login.html', error=error)


@application.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash("You've logged out")
    return redirect(url_for('index'))


if __name__ == '__main__':
    application.run(host='0.0.0.0')
