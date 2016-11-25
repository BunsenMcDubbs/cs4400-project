create table year_name (
  year int,
  name varchar(50),

  primary key (year, name)
);

insert into year_name (year, name)
values
  (2017, 'Senior'),
  (2018, 'Junior'),
  (2019, 'Sophomore'),
  (2020, 'Freshman');
