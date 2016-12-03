from app import db

class Category():
    @staticmethod
    def get_all():
        query = ("SELECT name FROM category")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        return all_data
