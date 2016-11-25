from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user

from app.forms import LoginForm, RegisterUserForm
from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    if not current_user.is_authenticated:
        return redirect(url_for('.login'))
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.find_by_username(username=form.username.data)
        login_user(user)
        flash('Welcome back %s!'%str(user.username), 'success')
        return redirect(request.args.get('next') or url_for('.home'))
    return render_template('login.html', form=form)

@main.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('.login'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterUserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            password=form.password.data,
            email=form.email.data
            )
        user.save()
        login_user(user)
        flash('Welcome %s!'%str(user.username), 'success')
        return redirect(request.args.get('next') or url_for('.home'))
    return render_template('register.html', form=form)
