import app.db as db

class Year():
    @staticmethod
    def convert_to_name(year):
        query = ("SELECT name FROM year_name WHERE year=%(year)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'year': year})
            name = cursor.fetchone()
        return name


    @staticmethod
    def convert_to_year(name):
        query = ("SELECT year from year_name WHERE name=%(name)s")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {'name': name})
            year = cursor.fetchone()
        return year

    @staticmethod
    def get_all():
        query = ("SELECT year, name from year_name")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query)
            all_data = list(cursor.fetchall())
        all_data.append({'name': 'None', 'year': None})
        return all_data
