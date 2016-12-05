import app.db as db

class Course():
    def __init__(self, course_number, name, instructor, est_num_students, designation_name, categories, is_new_course=True):
        self.course_number = course_number
        self.name = name
        self.instructor = instructor
        self.est_num_students = est_num_students
        self.designation_name = designation_name
        self.categories = categories
        self.is_new_course = is_new_course

    def save(self):
        insert_course = (
        "INSERT INTO course"
            "(name,"
            "course_number,"
            "instructor,"
            "est_num_students,"
            "designation_name)"
         "VALUES"
            "(%(name)s,"
            "%(course_number)s,"
            "%(instructor)s,"
            "%(est_num_students)s,"
            "%(designation_name)s)"
        )
        insert_category = (
        "INSERT INTO course_category (course_name, category_name)"
        "VALUES (%(name)s, %(category)s)"
        )
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            if self.is_new_course:
                cursor.execute(insert_course, vars(self))
                for c in filter(lambda c: c is not None, self.categories):
                    cursor.execute(insert_category, {'name': self.name, 'category': c})
            else:
                raise NotImplementedError('courses can not be modified')
            cnx.commit()
        self.is_new_course = False

    @staticmethod
    def find_by_name(name):
        query = (
        "SELECT "
            "name,"
            "course_number,"
            "instructor,"
            "est_num_students,"
            "designation_name "
        "FROM course "
        "WHERE name=%(name)s"
        )
        get_categories = (
        "SELECT category_name FROM course_category "
        "WHERE course_name=%(name)s")
        cnx = db.get_connection()
        course = None
        with cnx.cursor() as cursor:
            cursor.execute(query, {'name': name})
            data = cursor.fetchone()
            if data is not None:
                cursor.execute(get_categories, {'name': name})
                data['categories'] = cursor.fetchall()
                course = Course(is_new_course=False, **data)
        return course
