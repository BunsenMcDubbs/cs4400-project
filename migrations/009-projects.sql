insert into project (advisor_name, name, description, designation_name, est_num_students)
values
	(
		'Marie Williams',
        'Excel Peer Support Network',
        'Excel (www.excel.gatech.edu) is a four-year, dual certificate program for students with intellectual and developmental disabilities. The Peer Support Network is designed to provide the individualized support necessary for Excel students to thrive at Georgia Tech.',
        'community',
        60
    ),
    (
		'Nicole Kinnard',
        'ESW Hydroponics/Urban Farming Project',
        'ESW Hydroponics/Urban Farming Project	The Hydroponics/Urban Farming Project experiments with different ways to grow produce in urban areas using limited space and water resources. We investigate both soil-based and hydroponic methods of growing in order to find the most efficient, economically viable, and environmentally sustainable way to grow produce in Atlanta.',
        'sustainable communities',
        7
	),
    (
		'Ashley Bidlack',
        'Excel Current Events',
        'Excel Current Events is a participation (not for credit) course for degree-seeking students who are interested in developing their communication skills in conversations with adults with intellectual and developmental disabilities.',
        'community',
        15
	),
    (
        'Sarah Higinbotham',
        'Shakespeare in Prison Project',
        'As the world celebrates the 400th anniversary of Shakespeare’s death in 2016, Georgia Tech students will travel to a high-security men’s prison outside Atlanta to discuss Shakespeare with incarcerated students.',
        'community',
        20
	),
    (
		'Neha Kumar',
        'Know Your Water Project',
        'This project will allow students to be part of a large, crowd-sourced study – at little cost to themselves – to contribute to a knowledge bank of how different communities treat and track their water quality. If you are interested in participating in this study, please let us know.',
        'sustainable communities',
        10
	),
    (
		'Yeji Lee',
        'Epic Intentions',
        'Epic Intentions connects an interdisciplinary team of students with a local nonprofit to apply technical skills for social and civic good to help make the nonprofits make a greater impact in the community.',
        'community',
        20
	);

update project
set advisor_email = concat(lower(replace(advisor_name, ' ', '')), '@gatech.edu');

insert into project_category (project_name, category_name)
values
	('Excel Peer Support Network', 'computing for good'),
	('Excel Peer Support Network', 'doing good for your neighborhood'),
    ('Excel Peer Support Network', 'reciprocal teaching and learning'),
    ('ESW Hydroponics/Urban Farming Project', 'urban development'),
    ('ESW Hydroponics/Urban Farming Project', 'sustainable communities'),
    ('Excel Current Events', 'computing for good'),
    ('Excel Current Events', 'doing good for your neighborhood'),
    ('Excel Current Events', 'reciprocal teaching and learning'),
    ('Excel Current Events', 'technology for social good'),
    ('Shakespeare in Prison Project', 'urban development'),
    ('Shakespeare in Prison Project', 'sustainable communities'),
    ('Know Your Water Project', 'sustainable communities'),
    ('Know Your Water Project', 'crowd-sourced'),
    ('Epic Intentions', 'doing good for your neighborhood'),
    ('Epic Intentions', 'collaborative action');

insert into project_requirement (name, requirement)
values
	('Excel Peer Support Network', 'computer science'),
    ('Excel Peer Support Network', 'Senior'),
    ('ESW Hydroponics/Urban Farming Project', 'Junior'),
    ('Excel Current Events', 'college of computing'),
    ('Excel Current Events', 'Senior'),
    ('Shakespeare in Prison Project', 'college of design'),
    ('Know Your Water Project', 'computer science'),
    ('Know Your Water Project', 'Senior'),
    ('Epic Intentions', 'computer science'),
    ('Epic Intentions', 'Senior');