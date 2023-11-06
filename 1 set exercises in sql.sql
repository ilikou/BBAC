--Retrieve all information from the 'dataset' table
select *
from dataset;

--Retrieve the title, imprint, rating, number of ratings, and language
select title, imprint, rating_avg, rating_count,lang
from dataset;
--Which languages are present in the dataset table?
select distinct lang
from dataset
where lang notnull ;
--Find the books that have the word 'history' anywhere in their title
select *
from dataset where title like '%history%';
--Find the books in Spanish('hi)', Italian('it') and Greek('el')
select *
from dataset where lang in ('hi','it','el');
--Titles:Find the titles with the highest average ratings (rating = 5)
select max(rating_avg),title
from dataset where rating_avg=5
group by title;
--Titles:Which title(s) from this set have above 20 rating counts?
select max(rating_avg),rating_count,title
from dataset where rating_avg=5 and rating_count>20
group by title,rating_count;
--Which editor (imprint) published the highest number of titles between 2010 and 2020?
select imprint, count(title) as summary_book
from dataset
where publication_date between  '2010-01-01' and '2019-12-31'
and imprint notnull  
group by imprint
order by summary_book desc
limit 1;
--Format: Which is the most published format from MIT Press?
select count(format) as format_count
from dataset
where imprint = 'MIT Press'
group by format
order by format_count desc
limit 1;
--Which editors publish in leather format?
--How many books are in each format?
select count(title) as title_count
from dataset
group by format
order by title_count desc;
--Find the titles of the top 100 best sellers
SELECT title,bestsellers_rank
FROM dataset
ORDER BY bestsellers_rank asc 
LIMIT 100;
--Display the formats where the last characters are "back"
select *
from dataset;
