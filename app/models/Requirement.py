from app import db

class Requirement():
    @staticmethod
    def _get_by_type(r_type):
        query = (
        "SELECT requirement_name FROM requirement "
        "WHERE requirement_type=%(r_type)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'r_type': r_type})
            reqs = cursor.fetchall()
            reqs.append({'requirement_name': None})
        return reqs

    @staticmethod
    def get_all_year():
        return Requirement._get_by_type('year')
    
    @staticmethod
    def get_all_major():
        return Requirement._get_by_type('major')

    @staticmethod
    def get_all_department():
        return Requirement._get_by_type('department')
