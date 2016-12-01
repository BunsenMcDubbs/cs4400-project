from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

# from app.models import User
from app.forms import (
    AddProjectForm
)

admin = Blueprint('admin', __name__,)

@admin.route('/')
def home():
    return render_template('admin/index.html')

@admin.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm()
    return render_template('admin/add_project.html', form=form)
