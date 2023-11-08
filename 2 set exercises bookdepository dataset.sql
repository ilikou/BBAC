
--DAY 2
--What is the format name from users table where has the minimum count (display the minimum also)?
select *
from users; 

select format_name,min(count) as min_count
from users where count = (select min (count) from users)
group by format_name
order by min_count;

--Find the descriptions (from dataset) 
--with publication date in 2019 (sort them from 1st January until the end of the year)

select *
from HR_Database.public.employees
from dataset;
select description 
from dataset where publication_date between  '2019-01-01' and '2019-12-31'
and description notnull
group by description;

--Find how many descriptions (from dataset) doesn't have rating
select count(description)  as description_count
from dataset where rating_count isnull 







