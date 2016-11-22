from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

# from app.models import User

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

