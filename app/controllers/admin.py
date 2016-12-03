from flask import Blueprint, render_template, flash, request, redirect, url_for
from flask_login import login_user, logout_user, login_required

from app.models import (
    User,
    Project,
    Course,
    Application,
)
from app.forms import (
    AddProjectForm,
    AddCourseForm,
)

from app.admin_reports import (
    get_all_applications,
    get_popular_projects,
    get_application_report,
)

admin = Blueprint('admin', __name__,)

@admin.route('/')
def home():
    return render_template('admin/index.html')

@admin.route('/add_project', methods=['GET', 'POST'])
def add_project():
    form = AddProjectForm()
    if form.validate_on_submit():
        project = Project(
            name=form.name.data,
            description=form.description.data,
            advisor_name=form.advisor_name.data,
            advisor_email=form.advisor_email.data,
            est_num_students=form.est_num_students.data,
            designation_name=form.designation_name.data,
            categories=form.categories.data,
            requirements=[
                form.requirement_year.data,
                form.requirement_major.data,
                form.requirement_department.data,
                ],
            is_new_project=True,
            )
        project.save()
        return redirect(url_for('.home'))
    return render_template('admin/add_project.html', form=form)

@admin.route('/add_course', methods=['GET', 'POST'])
def add_course():
    form = AddCourseForm()
    if form.validate_on_submit():
        course = Course(
            course_number=form.course_number.data,
            name=form.name.data,
            instructor=form.instructor.data,
            est_num_students=form.est_num_students.data,
            designation_name=form.designation_name.data,
            categories=form.categories.data,
            is_new_course=True,
            )
        course.save()
        return redirect(url_for('.home'))
    return render_template('admin/add_course.html', form=form)

@admin.route('/applications')
def view_all_applications():
    applications = get_all_applications()
    return render_template('admin/view_all_applications.html', applications=applications)

@admin.route('/applications/<project_name>/<student_name>/accept')
def accept_application(project_name, student_name):
    return _decide_application(project_name, student_name, accept=True)

@admin.route('/applications/<project_name>/<student_name>/reject')
def reject_application(project_name, student_name):
    return _decide_application(project_name, student_name, accept=False)

def _decide_application(project_name, student_name, accept):
    application = Application.find(
        project_name=project_name,
        student_name=student_name)
    if application.status == 'pending':
        if accept:
            application.accept()
            flash('Successfully accepted application', 'success')
        else:
            application.reject()
            flash('Successfully rejected application', 'success')
    else:
        flash('Cannot change status of a decided application', 'danger')
    return redirect(url_for('admin.view_all_applications'))

@admin.route('/popular_projects')
def view_popular_projects():
    projects = get_popular_projects()
    return render_template('admin/view_popular_projects.html', projects=projects)

@admin.route('/view_application_report')
def view_application_report():
    projects = get_application_report()
    return render_template('admin/view_application_report.html', projects=projects)
