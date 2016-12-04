from app import db

def search(title=None,category=None,designation=None,major=None,year=None,project=True,course=True):
    course_str = "SELECT name, 'Course' AS type FROM course WHERE %s"
    project_str = "SELECT name, 'Project' AS type FROM project WHERE %s"
    title_str = "name = '%s'"
    course_category_str = "name IN (SELECT course_name FROM course_category WHERE category_name IN (%s))"
    project_category_str = "name IN (SELECT project_name FROM project_category WHERE category_name IN (%s))"
    designation_str = "designation_name = '%s'"
    requirement_str = "name IN (SELECT name FROM project_requirement WHERE requirement IN (%s))"
    
    # query parts
    course_qp = []
    project_qp = []
    
    if title is not None and len(title) != 0:
        course_qp.append(title_str%title)
        project_qp.append(title_str%title)
    if category is not None:
        category = filter(lambda c: c is not None, category)
        if len(category) != 0:
            category_str = ','.join(["'%s'"%c for c in category])
            course_qp.append(course_category_str%category_str)
            project_qp.append(project_category_str%category_str)
    if designation is not None:
        course_qp.append(designation_str%designation)
        project_qp.append(designation_str%designation)
    if major is not None or year is not None:
        in_clause = []
        if major is not None:
            in_clause.append("'%s'"%major)
        if year is not None:
            in_clause.append("'%s'"%year)
        project_qp.append(requirement_str%','.join(in_clause))

    if len(course_qp) == 0:
        course_qp.append('TRUE')
    if len(project_qp) == 0:
        project_qp.append('TRUE')

    query_parts = []
    if course:
        query_parts.append(course_str%' AND '.join(course_qp))
    if project:
        query_parts.append(project_str%' AND '.join(project_qp))
    
    query = ' UNION ALL '.join(query_parts)
    cnx = db.get_connection()
    with cnx.cursor() as cursor:
        try:
            cursor.execute(query)
            results = cursor.fetchall()
        finally:
            print cursor._last_executed
    return results
