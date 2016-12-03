create table requirement (
    requirement_name varchar(50),
    requirement_type varchar(50),

    primary key(requirement_name, requirement_type)
);

alter table project_requirement
    add constraint fk_project_requirement_name_requirement_requirement_name
    foreign key (name) references requirement(requirement_name);

insert into requirement (requirement_name, requirement_type)
values 
    ('computer science', 'major'),
    ('senior', 'year'),
    ('junior', 'year'),
    ('sophomore', 'year'),
    ('college of computing', 'department'),
    ('college of design', 'department')
