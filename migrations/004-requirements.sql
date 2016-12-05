create table requirement (
    requirement_name varchar(50),
    requirement_type varchar(50),

    primary key(requirement_name, requirement_type)
);

alter table project_requirement
    add constraint fk_project_requirement_requirement_requirement_requirement_name
    foreign key (requirement) references requirement(requirement_name);

insert into requirement (requirement_name, requirement_type)
select name, 'major' from major;

insert into requirement (requirement_name, requirement_type)
select department_name, 'department' from major group by department_name;

insert into requirement (requirement_name, requirement_type)
select name, 'year' from year_name;