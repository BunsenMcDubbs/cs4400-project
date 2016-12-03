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
            cursor.close()
        return projects if fuzzy else projects[0]

