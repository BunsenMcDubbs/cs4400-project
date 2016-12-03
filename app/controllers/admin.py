from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.models import (
    Project,
)
from app.forms import (
    AddProjectForm,
)

admin = Blueprint('admin', __name__,)

@admin.route('/')
def home():
    return render_template('admin/index.html')

@admin.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm()
    print vars(form)
    print 'validating...'
    if form.validate_on_submit():
        print 'valid!'
        project = Project(
            name=form.name.data,
            description=form.description.data,
            advisor_name=form.advisor_name.data,
            advisor_email=form.advisor_email.data,
            est_num_students=form.est_num_students.data,
            designation_name=form.designation_name.data,
            categories=form.categories.data,
            requirements=form.requirements.data,
            is_new_project=True,
            )
        project.save()
        return redirect(url_for('.home'))
    print 'failed!'
    return render_template('admin/add_project.html', form=form)
