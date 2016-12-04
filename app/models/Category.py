from app import db

class Category():
    @staticmethod
    def get_all(include_none=False):
        query = ("SELECT name FROM category")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        if include_none:
            all_data.insert(0, {'name': 'None'})
        return all_data
