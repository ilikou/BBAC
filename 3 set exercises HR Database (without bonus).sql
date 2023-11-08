--Sort the employees by their last name, their salary and their hire date

select *
from "HR Database".public.employees 
order by last_name; 

--Sort the employees their salary and their hire date
select *
from "HR Database".public.employees 
order by salary desc ;

--Sort the employees their hire date
select *
from "HR Database".public.employees 
order by hire_date ;



-- How many employees are there? How many departments and job specialties? (give a name to the new columns)
select count(distinct department_id) as department_count,count(employee_id) as employee_count,count(distinct job_id) as job_count
from employees 
order by department_count,employee_count,job_count;

--What is the average salary of all employees? How much is the company paying for salaries in total?
select avg(salary) as average_salary, sum(salary) as total_salary
from employees 
order by average_salary,total_salary;


--Who is getting the highest and who the lowest salary?
select max(salary) as max_salary,employee_id 
from employees 
group by employee_id 
order by max_salary desc 
limit 1; 

select min(salary) as minimum_salary,employee_id 
from employees 
group by employee_id 
order by minimum_salary asc  
limit 1;

--How many employees are working in each department? find the five departments with the most of them.
select department_id, count (employee_id) as count_employees_department
from employees 
group by department_id 
order by count_employees_department;

select department_id, count (employee_id) as count_employees_department
from employees 
group by department_id 
order by count_employees_department desc 
limit 5 ;

-- Find the five specialties with the most employees, too.
select job_id , count (employee_id) as count_employees_job
from employees 
group by job_id  
order by count_employees_job desc 
limit 5 ;

--Find how many employees were hired per department from 1990 to the end of 1995.
select count(employee_id) as count_employees
from employees where hire_date between '1990-01-01' and '1995-12-31'


