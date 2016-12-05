from random import randint, sample
from app.models import Category, Course, Designation

def add_courses(num_courses=12):
    course_titles = ['CS', 'ARCH', 'EAS', 'MECH', 'BIOL', 'BMED', 'ECE', 'HTS', 'LMC']
    designations = [d['name'] for d in Designation.get_all()]
    categories = [c['name'] for c in Category.get_all()]

    for i in xrange(num_courses):
        course_number='{} {}'.format(
            course_titles[randint(0, len(course_titles) - 1)],
            randint(1000, 9999))
        instructor='Instructor for {}'.format(course_number)
        designation = designations[randint(0, len(designations) - 1)]
        cats = [categories[i] for i in sample(xrange(len(categories)), randint(2, 5))]
        new_course = Course(
            course_number=course_number,
            name='Course Name for {}'.format(course_number),
            instructor=instructor,
            est_num_students=randint(0, 1000),
            designation_name=designation,
            categories=cats,
            is_new_course=True
        )
        new_course.save()

if __name__=='__main__':
    add_courses()
