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

