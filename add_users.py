from app.models import User, Year, Major
from random import randint

def add_admins(num_admins=5):
    for i in range(num_admins):
        name = 'admin{}'.format(i)
        password = 'admin'
        email = '{}@gatech.edu'.format(name)
        new_admin = User(
            username=name,
            password=password,
            email=email,
            is_admin=True)
        new_admin.save()

def add_users():
    names = [
        'andrew',
        'brian',
        'connor',
        'david',
        'elise',
        'francis',
        'gerald',
        'hillary',
        'isabela',
        'jennifer',
        'kelly',
        'lisa',
        'mona',
        'natalie',
        'oswald',
        'peter',
        'quincy',
        'richard',
        'sarah',
        'timothy',
        'uma',
        'valerie',
        'wally',
        'xavier',
        'yamini',
        'zachary'
        ]
    years = [year['year'] for year in Year.get_all()]
    majors = [major['name'] for major in Major.get_all()]
    remaining_with_majors = 20
    for name in names:
        email = '{}@gatech.edu'.format(name)
        year = years[randint(0, len(years) - 1)]
        major = None if remaining_with_majors <= 0 else majors[randint(0, len(majors) - 1)]
        remaining_with_majors -= 1
        new_user = User(
            username=name,
            password=name,
            email=email,
            year=year,
            major=major)
        new_user.save()

if __name__=='__main__':
    add_admins()
    add_users()        
