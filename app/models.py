from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import app.db as db

class User(UserMixin):
    def __init__(self, username, password, email, year=None, major=None, is_admin=False, is_new_user=True):
        self.username = username
        self.password = password if is_new_user is False else generate_password_hash(password)
        self.email = email
        self.year = year
        self.major = major
        self.is_admin = is_admin == True
        self.is_new_user = is_new_user

    def save(self):
        insert_user = "INSERT INTO user (username, password, email, year, major, is_admin) VALUES (%(username)s, %(password)s, %(email)s, %(year)s, %(major)s, %(is_admin)s)"
        update_user = "UPDATE user SET email=%(email)s, year=%(year)s, major=%(major)s WHERE username=%(username)s"
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            try:
                if self.is_new_user:
                    cursor.execute(insert_user, vars(self))
                    self.is_new_user = False
                else:
                    cursor.execute(update_user, vars(self))
            except:
                print cursor._last_executed
                raise
            cnx.commit()

    def set_password(self, password):
        password_hash = generate_password_hash(password)
        set_password = "UPDATE user SET password=%(password)s WHERE username=%(username)s"
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            result = cursor.execute(set_password, {
                'username': self.username,
                'password': password_hash,
            })
            cnx.commit()
        return result
        # return {'error': 'not yet implemented'}

    def check_password(self, value):
        return check_password_hash(self.password, value)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username

    @staticmethod
    def find_by_username(username):
        query = ("SELECT username, password, email, year, major, is_admin FROM user WHERE username=%(username)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'username': username})
            raw_data = cursor.fetchone()
            user = User(is_new_user=False, **raw_data) if raw_data is not None else None
        return user

class Year():
    @staticmethod
    def convert_to_name(year):
        query = ("SELECT name FROM year_name WHERE year=%(year)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'year': year})
            name = cursor.fetchone()
        return name


    @staticmethod
    def convert_to_year(name):
        query = ("SELECT year from year_name WHERE name=%(name)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'name': name})
            year = cursor.fetchone()
        return year

    @staticmethod
    def get_all():
        query = ("SELECT year, name from year_name")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        all_data.append({'name': 'None', 'year': None})
        return all_data

class Major():
    @staticmethod
    def get_department(major):
        query = ("SELECT department FROM major WHERE major=%(major)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'major': major})
            dept = cursor.fetchone()
        return dept

    @staticmethod
    def get_all():
        query = ("SELECT name, department_name FROM major")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        all_data.append({'name': 'None'})
        return all_data

class Project():

    def __init__(self, name, description, advisor_name, advisor_email, est_num_students, designation_name, categories, requirements=list(), is_new_project=True):
        self.name = name
        self.description = description
        self.advisor_name = advisor_name
        self.advisor_email = advisor_email
        self.est_num_students = est_num_students
        self.designation_name = designation_name
        self.categories = categories
        self.requirements = requirements
        self.is_new_project = is_new_project

    def save(self):
        insert_project = (
        "INSERT INTO project "
            "(name,"
            "description,"
            "advisor_name,"
            "advisor_email,"
            "est_num_students,"
            "designation_name)"
        "VALUES ("
            "%(name)s,"
            "%(description)s,"
            "%(advisor_name)s,"
            "%(advisor_email)s,"
            "%(est_num_students)s,"
            "%(designation_name)s)")
        insert_category = (
        "INSERT INTO project_category (project_name, category_name) "
        "VALUES (%(name)s, %(category)s)"
        )
        insert_requirement = (
        "INSERT INTO project_requirement (name, requirement) "
        "VALUES (%(name)s, %(requirement)s)"
        )

        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            project_dict = {
                'name': self.name,
                'description': self.description,
                'advisor_name': self.advisor_name,
                'advisor_email': self.advisor_email,
                'est_num_students': self.est_num_students,
                'designation_name': self.designation_name,
            }
            if self.is_new_project:
                cursor.execute(insert_project, project_dict)
                for c in filter(lambda c: c is not None, self.categories):
                    cursor.execute(insert_category, {'category': c, 'name': self.name})
                for r in filter(lambda r: r is not None, self.requirements):
                    cursor.execute(insert_requirement, {'requirement': r, 'name': self.name})
            else:
                raise NotImplementedError('projects can not be modified')
            cnx.commit()

    @staticmethod
    def find_by_name(name, fuzzy=False):
        query = (
        "SELECT "
            "name, "
            "description, "
            "advisor_name, "
            "advisor_email, "
            "est_num_students, "
            "designation_name "
        "FROM project WHERE name like %(name)s")
        get_categories = ("SELECT category_name FROM project_category WHERE project_name=%(name)s")
        get_requirements = ("SELECT requirement FROM project_requirement WHERE name=%(name)s")
        
        # if fuzzy search, then name should become '%<name>%'
        # ex) name = 'andrew' => name = '%andrew%'
        name = name if fuzzy is False else '%%%s%%'%(name)
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            projects = list()
            cursor.execute(query, {'name': name})
            for result in cursor:
                data = dict(result)
                p = Project(is_new_project=False, categories=[], requirements=[], **data)
                projects.append(p)
            for p in projects:
                cursor.execute(get_categories, {'name': p.name})
                p.categories = cursor.fetchall()
                cursor.execute(get_requirements, {'name': p.name})
                p.requirements = cursor.fetchall()
        return projects if fuzzy else projects[0]

class Course():
    def __init__(self, course_number, name, instructor, est_num_students, designation_name, categories, is_new_course=True):
        print type(course_number)
        self.course_number = course_number
        self.name = name
        self.instructor = instructor
        self.est_num_students = est_num_students
        self.designation_name = designation_name
        self.categories = categories
        self.is_new_course = is_new_course
    
    def save(self):
        insert_course = (
        "INSERT INTO course"
            "(name,"
            "course_number,"
            "instructor,"
            "est_num_students,"
            "designation_name)"
         "VALUES"
            "(%(name)s,"
            "%(course_number)s,"
            "%(instructor)s,"
            "%(est_num_students)s,"
            "%(designation_name)s)"
        )
        insert_category = (
        "INSERT INTO course_category (course_name, category_name)"
        "VALUES (%(name)s, %(category)s)"
        )
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            if self.is_new_course:
                cursor.execute(insert_course, vars(self))
                for c in filter(lambda c: c is not None, self.categories):
                    cursor.execute(insert_category, {'name': self.name, 'category': c})
            else:
                raise NotImplementedError('courses can not be modified')
            cnx.commit()
        self.is_new_course = False

    @staticmethod
    def find_by_name(name):
        query = (
        "SELECT "
            "name,"
            "course_number,"
            "instructor,"
            "est_num_students,"
            "designation_name "
        "FROM course "
        "WHERE name=%(name)s"
        )
        get_categories = (
        "SELECT category_name FROM course_category "
        "WHERE course_name=%(name)s")
        cnx = db.get_connection()
        course = None
        with cnx.cursor() as cursor:
            cursor.execute(query, {'name': name})
            data = cursor.fetchone()
            if data is not None:
                cursor.execute(get_categories, {'name': name})
                data['categories'] = cursor.fetchall()
                course = Course(is_new_course=False, **data)
        return course

class Application():
    def __init__(self, project_name, student_name, application_date, status='pending', is_new_application=True):
        self.project_name = project_name
        self.student_name = student_name
        self.application_date = application_date
        self.status = status
        self.is_new_application = is_new_application
    
    def accept(self):
        if self.is_new_application:
            raise ValueError('cannot approve a new application, save first')
        self._update_status('accepted')

    def reject(self):
        if self.is_new_application:
            raise ValueError('cannot reject a new application, save first')
        self._update_status('rejected')

    def _update_status(self, new_status):
        update_query = (
        "UPDATE application SET status=%(status)s "
        "WHERE "
            "project_name=%(project_name)s and "
            "student_name=%(student_name)s")

        self.status = new_status
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(update_query, vars(self))
            cnx.commit()

    def save(self):
        insert_application = (
        "INSERT INTO application "
            "(project_name,"
            "student_name,"
            "application_date,"
            "status) "
        "VALUES "
            "(%(project_name)s,"
            "%(student_name)s,"
            "%(application_date)s,"
            "%(status)s)")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            if self.is_new_application:
                cursor.execute(insert_application, vars(self))
            else:
                raise NotImplementedError('courses can not be modified')
            cnx.commit()
        self.is_new_application = False

    @staticmethod
    def find(student_name='%%', project_name='%%'):
        query = (
        "SELECT "
            "project_name,"
            "student_name,"
            "application_date,"
            "status "
        "FROM application "
        "WHERE "
            "project_name LIKE %(project_name)s and "
            "student_name LIKE %(student_name)s")
        multi = student_name == '%%' or project_name == '%%'
        results = list() if multi else None
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {
                'project_name': project_name,
                'student_name': student_name,
            })
            for result in cursor:
                if multi:
                    results.append(Application(is_new_application=False, **result))
                else:
                    results = Application(is_new_application=False, **result)
        return results

