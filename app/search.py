from app import db

def search():
    query = (
    "SELECT name, 'Course' as type FROM course "
    "UNION "
    "SELECT name, 'Project' as type FROM project"
    )
    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return results
