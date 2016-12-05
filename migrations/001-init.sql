create table user (
  username varchar(50) primary key,
  password varchar(100) not null,
  email varchar(50) unique,
  year int,
  major varchar(50),
  is_admin boolean not null default false
);

create table year_name (
  year int,
  name varchar(50),

  primary key (year, name)
);

create table project (
  name varchar(200) primary key,
  description varchar(1000),
  advisor_email varchar(50),
  advisor_name varchar(50),
  est_num_students int,
  designation_name varchar(50)
);

create table project_requirement (
  name varchar(200),
  requirement varchar(50),

  primary key(name, requirement)
);

create table designation (
  name varchar(50) primary key
);

create table category (
  name varchar(50) primary key
);

create table major (
  name varchar(50) primary key,
  department_name varchar(50) not null
);

create table department (
  name varchar(50) primary key
);

create table course (
  name varchar(200) primary key,
  course_number varchar(50),
  instructor varchar(50),
  est_num_students int,
  designation_name varchar(50)
);

create table application (
  project_name varchar(200),
  student_name varchar(50),
  application_date date not null,
  status enum('pending', 'accepted', 'rejected') not null,

  primary key (project_name, student_name)
);

create table project_category (
  project_name varchar(200),
  category_name varchar(50),

  primary key (project_name, category_name)
);

create table course_category (
  course_name varchar(200),
  category_name varchar(50),

  primary key (course_name, category_name)
);

alter table user
  add constraint fk_user_major_major_name
  foreign key (major) references major(name);

alter table project
  add constraint fk_project_designation_name_designation_name
  foreign key (designation_name) references designation(name);

alter table project_requirement
  add constraint fk_project_requirement_name_project_name
  foreign key (name) references project(name);

alter table major
  add constraint fk_major_department_name_department_name
  foreign key (department_name) references department(name);

alter table course
  add constraint fk_course_designation_name_designation_name
  foreign key (designation_name) references designation(name);

alter table application
  add constraint fk_application_project_name_project_name
  foreign key (project_name) references project(name),
  add constraint fk_application_student_name_user_username
  foreign key (student_name) references user(username);

alter table project_category
  add constraint fk_project_category_project_name_project_name
  foreign key (project_name) references project(name),
  add constraint fk_project_category_category_name_category_name
  foreign key (category_name) references category(name);

alter table course_category
  add constraint fk_course_category_course_name_course_name
  foreign key (course_name) references course(name),
  add constraint fk_course_category_category_name_category_name
  foreign key (category_name) references category(name);

