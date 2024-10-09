from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('gmail')
        password = request.form.get('password')
        user = User.query.filter_by(email = email).first()
        if User:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category='success')
                return redirect(url_for('views.index'))
            else:
                flash("Incorrect password, try again.", category='error')
        else:
            flash("Email doesn't exixt.", category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>hello</p>"

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('gmail')
        name = request.form.get('name')
        password1 = request.form.get('password')
        password2 = request.form.get('cnfm-passwd')

        user = User.query.filter_by(email = email).first()
        if user:
            flash("Email already exixts", category='error')
        elif len(email) < 4:
            flash('email must be greater than 3 characters.', category='error')
        elif len(name) < 2:
            flash('name must be greater than 1 characters.', category='error')
        elif password1 != password2:
            flash('passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('password must be greater than 7 characters.', category='error')
        else:
            new_user = User(email = email, name = name, password = generate_password_hash(password1, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('views.index'))

    return render_template('sign_up.html')