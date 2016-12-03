from app import db
from app.models import User, Application

def get_all_applications():
    query = (
    "SELECT project_name, student_name, major, year, status "
    "FROM admin_application_view")
    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def get_popular_projects():
    query = (
    "SELECT project_name, num_applicants "
    "FROM admin_popular_project")
    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        return cursor.fetchall()

def get_application_report():
    get_applications = (
    "SELECT project_name, num_applicants, accept_rate "
    "FROM admin_application_report")
    get_majors = (
    "SELECT major "
    "FROM admin_application_report_top_majors "
    "WHERE project_name=%(project_name)s")
    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        cursor.execute(get_applications)
        projects = cursor.fetchall()
        for project in projects:
            cursor.execute(get_majors, {'project_name': project['project_name']})
            project['majors'] = [result['major'] for result in cursor.fetchall()][:3]
    return projects
