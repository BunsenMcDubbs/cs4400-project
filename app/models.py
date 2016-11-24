from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

import app.db as db

class User():
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
        cursor = cnx.cursor()
        if self.is_new_user:
            cursor.execute(insert_user, vars(self))
            self.is_new_user = False
        else:
            cursor.execute(update_user, vars(self))
        cnx.commit()
        cursor.close()


    def set_password(self, password):
        password_hash = generate_password_hash(password)
        set_password = "UPDATE user SET password=%(password)s WHERE username=%(username)s"
        cnx = db.get_connection()
        cursor = cnx.cursor()
        result = cursor.execute(set_password, {
            'username': self.username,
            'password': password_hash,
        })
        cnx.commit()
        cursor.close()
        return result
        # return {'error': 'not yet implemented'}

    def check_password(self, value):
        return check_password_hash(self.password, value)

    @staticmethod
    def find_by_username(username):
        query = ("SELECT username, password, email, year, major, is_admin FROM user WHERE username=%(username)s")
        cnx = db.get_connection()
        cursor = cnx.cursor()
        cursor.execute(query, {'username': username})
        raw_data = cursor.fetchone()
        user = User(raw_data[0], raw_data[1], raw_data[2], is_new_user=False, extra_info={
            'year': raw_data[3],
            'major': raw_data[4],
            'is_admin': raw_data[5],
        })
        cursor.close()
        return user
