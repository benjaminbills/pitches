from flask import render_template,redirect,url_for, flash,request
from flask_login import login_user, login_required, logout_user
from ..models import User
from . import auth
from .. import db

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user is not None and user.verify_password(password):
            login_user(user, remember=True)
            return redirect(request.args.get('next') or url_for('main.index'))
        print('Invalid username or Password')
    return render_template('auth/login.html')

@auth.route('/register',methods = ["GET","POST"])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        username = request.form.get('username')
        user = User(email = email, password = password, username = username)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')
