drop view if exists admin_application_view;
create view admin_application_view as (
    select
        a.project_name as project_name,
        a.student_name as student_name,
        u.major as major,
        u.year as year,
        a.status as status
    from application a
    join user u
        on a.student_name = u.username
);

drop view if exists admin_project_application_count;
create view admin_project_application_count as (
    select
        project_name,
        count(*) as num_applicants
    from application
    group by project_name
    order by num_applicants desc
);

drop view if exists admin_popular_project;
create view admin_popular_project as (
    select
        project_name,
        num_applicants
    from admin_project_application_count
    limit 10
);

drop view if exists admin_application_report;
create view admin_application_report as (
    select
        a.project_name as project_name,
        a.num_applicants as num_applicants,
        case when c.num_decided > 0 then c.num_accepted / c.num_decided else null end as accept_rate
    from admin_project_application_count a
    join (
        select
            project_name,
            sum(case when status='accepted' then 1 else 0 end) as num_accepted,
            sum(case when status='accepted' or status='rejected' then 1 else 0 end) as num_decided
        from application
        group by project_name
    ) c
    on a.project_name = c.project_name
    order by accept_rate desc
);

drop view if exists admin_application_report_top_majors;
create view admin_application_report_top_majors as (
    select
        a.project_name as project_name,
        u.major as major,
        count(*) as num_applicants
    from application a
    join user u
    on a.student_name = u.username
    group by a.project_name, u.major
    order by a.project_name, num_applicants
);
