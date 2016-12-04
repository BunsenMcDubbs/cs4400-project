from app import db

def search(title=None,category=None,designation=None,major=None,year=None,project=True,course=True):
    course_str = "SELECT name, 'Course' as type FROM course WHERE true "
    project_str = "SELECT name, 'Project' as type FROM project WHERE true "
    # search_str = []
    title_str = "AND name = '{}' "
    course_category_str = "AND name IN (SELECT course_name FROM course_category "
    project_category_str = "AND name IN (SELECT project_name FROM project_category "
    designation_str = "AND designation_name = '{}' "
    restriction_str = "name IN (SELECT project_name FROM project_requirement "

    if title != None:
        title_str = title_str.format(title)
        course_str += title_str
        project_str += title_str
    if category != None:
        cat_str = "WHERE category_name IN ("
        for item in category:
            cat_str += "'{}',".format(item)
        cat_str = cat_str[:-1] # remove trailing comma
        cat_str += ") ) "
        course_str += course_category_str + cat_str
        project_str += project_category_str + cat_str

    # designation, major, and year only for projects
    if designation != None:
        designation_str = designation_str.format(designation)
        project_str += designation_str
    if major != None or year != None:
        res_str = "WHERE requirement IN ("
        if major != None:
            res_str += "'{}',".format(major)
        if year != None:
            res_str += "{},".format(year)
        res_str = res_str[:-1] # remove trailing comma
        res_str += ") )"
        restriction_str += res_str
        course_str += restriction_str
        project_str += restriction_str

    query = course_str + "UNION " + project_str
    if project == False:
        query = course_str
    if course == False:
        query = project_str

    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        cursor.execute(query)
        results = cursor.fetchall()
    return results
