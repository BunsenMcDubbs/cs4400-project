import app.db as db
from app.models.Requirement import Requirement
from app.models.Major import Major
from app.models.Year import Year

class Project():

    def __init__(self, name, description, advisor_name, advisor_email, est_num_students, designation_name, categories, requirements=list(), is_new_project=True):
        self.name = name
        self.description = description
        self.advisor_name = advisor_name
        self.advisor_email = advisor_email
        self.est_num_students = est_num_students
        self.designation_name = designation_name
        self.categories = categories
        self.requirements = requirements
        self.is_new_project = is_new_project

    def save(self):
        insert_project = (
        "INSERT INTO project "
            "(name,"
            "description,"
            "advisor_name,"
            "advisor_email,"
            "est_num_students,"
            "designation_name)"
        "VALUES ("
            "%(name)s,"
            "%(description)s,"
            "%(advisor_name)s,"
            "%(advisor_email)s,"
            "%(est_num_students)s,"
            "%(designation_name)s)")
        insert_category = (
        "INSERT INTO project_category (project_name, category_name) "
        "VALUES (%(name)s, %(category)s)"
        )
        insert_requirement = (
        "INSERT INTO project_requirement (name, requirement) "
        "VALUES (%(name)s, %(requirement)s)"
        )
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            project_dict = {
                'name': self.name,
                'description': self.description,
                'advisor_name': self.advisor_name,
                'advisor_email': self.advisor_email,
                'est_num_students': self.est_num_students,
                'designation_name': self.designation_name,
            }
            if self.is_new_project:
                cursor.execute(insert_project, project_dict)
                for c in filter(lambda c: c is not None, self.categories):
                    cursor.execute(insert_category, {'category': c, 'name': self.name})
                for r in filter(lambda r: r is not None, self.requirements):
                    try:
                        cursor.execute(insert_requirement, {'requirement': r, 'name': self.name})
                    finally:
                        print cursor._last_executed
            else:
                raise NotImplementedError('projects can not be modified')
            cnx.commit()

    def check_user(self, user):
        for req in self.requirements:
            requirement_type = Requirement.get_type(req)
            if requirement_type == 'year':
                year_name = Year.convert_to_name(user.year)
                if year_name != req:
                    return False
            elif requirement_type == 'major':
                if user.major != req:
                    return False
            elif requirement_type == 'department':
                department = Major.get_department(user.major)
                if department != req:
                    return False
        return True

    @staticmethod
    def find_by_name(name, fuzzy=False):
        query = (
        "SELECT "
            "name, "
            "description, "
            "advisor_name, "
            "advisor_email, "
            "est_num_students, "
            "designation_name "
        "FROM project WHERE name like %(name)s")
        get_categories = ("SELECT category_name FROM project_category WHERE project_name=%(name)s")
        get_requirements = ("SELECT requirement FROM project_requirement WHERE name=%(name)s")

        # if fuzzy search, then name should become '%<name>%'
        # ex) name = 'andrew' => name = '%andrew%'
        name = name if fuzzy is False else '%%%s%%'%(name)
        cnx = db.get_connection()
        with cnx.cursor() as cursor:
            projects = list()
            cursor.execute(query, {'name': name})
            for result in cursor:
                data = dict(result)
                p = Project(is_new_project=False, categories=[], requirements=[], **data)
                projects.append(p)
            for p in projects:
                cursor.execute(get_categories, {'name': p.name})
                p.categories = cursor.fetchall()
                cursor.execute(get_requirements, {'name': p.name})
                p.requirements = cursor.fetchall()
        return projects if fuzzy else projects[0]
