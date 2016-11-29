from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import app.db as db

class User(UserMixin):
    def __init__(self, username, password, email, is_new_user=True, extra_info=dict()):
        self.username = username
        self.password = password if is_new_user is False else generate_password_hash(password)
        self.email = email
        self.year = extra_info.get('year', None)
        self.major = extra_info.get('major', None)
        self.is_admin = extra_info.get('is_admin', False)
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
            finally:
                print cursor._last_executed
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
            user = User(raw_data[0], raw_data[1], raw_data[2], is_new_user=False, extra_info={
                'year': raw_data[3],
                'major': raw_data[4],
                'is_admin': raw_data[5],
            }) if raw_data is not None else None
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
        all_data.append(('', 'None'))
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
        all_data.append(('', 'None'))
        return all_data
