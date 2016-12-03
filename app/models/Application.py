import app.db as db

class Application():
    def __init__(self, project_name, student_name, application_date, status='pending', is_new_application=True):
        self.project_name = project_name
        self.student_name = student_name
        self.application_date = application_date
        self.status = status
        self.is_new_application = is_new_application
    
    def accept(self):
        if self.is_new_application:
            raise ValueError('cannot approve a new application, save first')
        self._update_status('accepted')

    def reject(self):
        if self.is_new_application:
            raise ValueError('cannot reject a new application, save first')
        self._update_status('rejected')

    def _update_status(self, new_status):
        update_query = (
        "UPDATE application SET status=%(status)s "
        "WHERE "
            "project_name=%(project_name)s and "
            "student_name=%(student_name)s")

        self.status = new_status
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(update_query, vars(self))
            cnx.commit()

    def save(self):
        insert_application = (
        "INSERT INTO application "
            "(project_name,"
            "student_name,"
            "application_date,"
            "status) "
        "VALUES "
            "(%(project_name)s,"
            "%(student_name)s,"
            "%(application_date)s,"
            "%(status)s)")
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            if self.is_new_application:
                cursor.execute(insert_application, vars(self))
            else:
                raise NotImplementedError('courses can not be modified')
            cnx.commit()
        self.is_new_application = False

    @staticmethod
    def find(student_name='%%', project_name='%%'):
        query = (
        "SELECT "
            "project_name,"
            "student_name,"
            "application_date,"
            "status "
        "FROM application "
        "WHERE "
            "project_name LIKE %(project_name)s and "
            "student_name LIKE %(student_name)s")
        multi = student_name == '%%' or project_name == '%%'
        results = list() if multi else None
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            cursor.execute(query, {
                'project_name': project_name,
                'student_name': student_name,
            })
            for result in cursor:
                if multi:
                    results.append(Application(is_new_application=False, **result))
                else:
                    results = Application(is_new_application=False, **result)
        return results

