from app import db

class Designation():
    @staticmethod
    def get_all():
        query = ("SELECT name FROM designation")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = cursor.fetchall()
        return all_data
            
