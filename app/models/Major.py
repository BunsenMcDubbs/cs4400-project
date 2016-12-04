import app.db as db

class Major():
    @staticmethod
    def get_department_mapping():
        query = ("SELECT name, department_name FROM major")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            mapping = dict([(m['name'], m['department_name']) for m in cursor.fetchall()])
        return mapping

    @staticmethod
    def get_department(major):
        query = (
        "SELECT department_name FROM major WHERE name=%(major)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'major': major})
            department = cursor.fetchone()['department_name']
        return department

    @staticmethod
    def get_all(include_none=False):
        query = ("SELECT name, department_name FROM major")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        if include_none:
            all_data.insert(0, {'name': 'None'})
        return all_data

