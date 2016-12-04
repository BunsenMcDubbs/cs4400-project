from app import db

class Requirement():
    @staticmethod
    def get_type(requirement):
        query = (
        "SELECT requirement_type FROM requirement "
        "WHERE requirement_name=%(requirement)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'requirement': requirement})
            r_type = cursor.fetchone()['requirement_type']
        return r_type

    @staticmethod
    def _get_by_type(r_type, include_none=False):
        query = (
        "SELECT requirement_name FROM requirement "
        "WHERE requirement_type=%(r_type)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'r_type': r_type})
            reqs = cursor.fetchall()
            if include_none:
                reqs.append({'requirement_name': None})
        return reqs

    @staticmethod
    def get_all_year(include_none=False):
        return Requirement._get_by_type('year', include_none=include_none)
    
    @staticmethod
    def get_all_major(include_none=False):
        return Requirement._get_by_type('major', include_none=include_none)

    @staticmethod
    def get_all_department(include_none=False):
        return Requirement._get_by_type('department', include_none=include_none)
