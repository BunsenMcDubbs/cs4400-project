insert into course (instructor, course_number, name, designation_name, est_num_students)
values
	(	
		'Richard Dagenhart',
		'ARCH 4803',
        'Green Infrastructure: EPA Campus Rainwater Challenge',
        'sustainable communities',
        26
	),
    (
		'Barbara Burks Fasse',
        'BMED 2250',
        'Problems in Biomedical Engineering',
        'community',
        300
    ),
    (
		'Alice Favero',
        'PUBP 3315',
        'Environmental Policy and Politics',
        'sustainable communities',
        25
    ),
    (
		'Monica Halka',
        'EAS 2803',
        'Urban Forest',
        'sustainable communities',
        10
	),
    (
		'Brian Hammer',
        'BIOL 1511',
        'Honors Biological Principles; Honors Organismal Biology',
        'sustainable communities',
        150
	),
    (
		'Dana Hartley',
        'EAS 1600',
        'Introduction to Environmental Science',
        'community',
        600
	),
    (
		'Dana Hartley',
        'EAS 1601',
        'Habitable Planet',
        'community',
        600
	),
    (
		'Dana Hartley',
        'EAS 2750',
        'Physics of the Weather',
        'community',
        30
    );

insert into course_category (course_name, category_name)
values
	('Green Infrastructure: EPA Campus Rainwater Challenge', 'computing for good'),
    ('Green Infrastructure: EPA Campus Rainwater Challenge', 'doing good for your neighborhood'),
    ('Problems in Biomedical Engineering', 'computing for good'),
    ('Problems in Biomedical Engineering', 'doing good for your neighborhood'),
    ('Environmental Policy and Politics', 'urban development'),
    ('Environmental Policy and Politics', 'sustainable communities'),
    ('Urban Forest', 'urban development'),
    ('Urban Forest', 'sustainable communities'),
    ('Honors Biological Principles; Honors Organismal Biology', 'sustainable communities'),
    ('Introduction to Environmental Science', 'urban development'),
    ('Introduction to Environmental Science', 'sustainable communities'),
    ('Habitable Planet', 'urban development'),
    ('Habitable Planet', 'sustainable communities'),
    ('Physics of the Weather', 'urban development'),
    ('Physics of the Weather', 'sustainable communities');    