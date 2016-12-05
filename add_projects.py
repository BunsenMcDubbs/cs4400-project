from random import randint, sample, choice
from app.models import Category, Designation, Project, Requirement

def add_projects(num_projects=20):
    designations = [d['name'] for d in Designation.get_all()]
    categories = [c['name'] for c in Category.get_all()]
    year = [y['requirement_name'] for y in Requirement.get_all_year(include_none=True)]
    major = [m['requirement_name'] for m in Requirement.get_all_major(include_none=True)]
    department = [d['requirement_name'] for d in Requirement.get_all_department(include_none=True)]

    for i in xrange(num_projects):
        name = 'Project #{}'.format(i)
        description = 'Description for {}'.format(name)
        advisor_name = 'Advisor for {}'.format(name)
        advisor_email = 'project{}advisor@gatech.edu'.format(i)
        est_num_students = randint(0, 1000)
        designation = designations[randint(0, len(designations) - 1)]
        cats = [categories[i] for i in sample(xrange(len(categories)), randint(2, 5))]
        reqs = []
        if choice([True, False]):
            reqs.append(year[randint(0, len(year) - 1)])
        if choice([True, False]):
            reqs.append(major[randint(0, len(major) - 1)])
        else:
            reqs.append(major[randint(0, len(department) - 1)])

        new_project = Project(
            name=name,
            description=description,
            advisor_name=advisor_name,
            advisor_email=advisor_email,
            est_num_students=est_num_students,
            designation_name=designation,
            categories=cats,
            requirements=reqs,
            is_new_project=True
        )
        new_project.save()

if __name__=='__main__':
    add_projects()
