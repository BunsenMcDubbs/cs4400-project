from app import db

class Designation():
    @staticmethod
    def get_all(include_none=False):
        query = ("SELECT name FROM designation")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = cursor.fetchall()
        if include_none:
            all_data.insert(0, {'name': 'None'})
        return all_data
            
