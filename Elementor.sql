--------1-------------
SELECT
employee_id,
first_name,
last_name,
hire_date,
salary,
manager_id,
department_id
FROM (
 select
 employee_id,
 first_name,
 last_name,
 hire_date,
 salary,
 manager_id,
 department_id,
 salary -ifnull(lead(salary) OVER (partition by department_id ORDER BY salary desc ),salary) as difference,
 ROW_NUMBER() over(partition by department_id ORDER BY salary desc) as row_id
 from employees
)
where row_id=1

------2-----------------
with  site_visitors as (
SELECT
date,
site,
number_of_visitors,
case when promotion_code  is not null then 1 else 0 end promotion_date
FROM site_visitors site
left join promotion_dates prom
on site.site=prom.site
and date between prom.start_date and prom.end_date
)
select
(SELECT SUM(number_of_visitors) from site_visitors where promotion_date>0)*100.0 / (SELECT SUM(number_of_visitors) from site_visitors)*100.0 as ptc
from site_visitors
