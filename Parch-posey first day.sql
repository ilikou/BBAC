--1a. Look for companies which have the word 'group' anywhere in their names (case insensitive search)

select *
from accounts a ;

select accounts."name" as groups_names
from accounts 
where accounts."name" ilike '%Group%';

--1b. Remove (replace) the 'www.' and '.com' FROM the website column

select accounts.website,replace (replace (website,'www.','') ,'.com','')
from accounts ;

--2a. Find the position of ' ' (space) in the representatives' names
select *
from sales_reps ;

select sales_reps."name" ,position (' ' in "name")
from sales_reps 

--2b. Now create two columns for the first and last names of the representatives

select sales_reps."name",substring("name" from 1 for position(' ' in "name") - 1) as first_name ,substring ("name" from  position(' ' in "name") +1) as last_name
from sales_reps 

--3a. Create a column 'client_representative' in alphabetical order combining the name of the client company 
--and the name of the representative.

select
	sales_reps."name" as reps_name,
	accounts."name" as company_name
from
	accounts
inner join sales_reps on
	sales_reps.id = accounts.sales_rep_id
group by
	accounts."name" ,
	sales_reps."name";

--3b. How many clients does each representative have?

select sales_reps."name" ,count(accounts.id)
from accounts join sales_reps ON accounts.sales_rep_id = sales_reps.id
group  by sales_reps.name
order BY sales_reps.name;

--4a. Create a column coordinates combining latitude and longitude separated with a comma

select concat(lat, ' , ', long) as coordinates from accounts;

--4b. Create a column 'location' for each client combining latitude,
-- longitude and the region each representative is appointed ## at, separated with a comma.

select  accounts.name, accounts.lat, accounts.long, region.name as region ,concat(lat,' , ', long, ' , ', region.name) as location
from accounts
join sales_reps on accounts.sales_rep_id = sales_reps.id
join region on sales_reps.region_id = region.id;

--4c. When was the last entry of an order?

select max(occurred_at) from orders;

--4d. How long since this last entry?

select age(current_timestamp, max(occurred_at)) from orders;