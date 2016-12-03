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
    def get_all():
        query = ("SELECT name, department_name FROM major")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        all_data.append({'name': 'None'})
        return all_data

