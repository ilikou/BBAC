--Dataset: lahman2017


--1. Which player hit the most home runs in 2002?


select *
from homegames h ;

select *
from appearances a ;

select * 
from batting b ;

select playerid,yearid ,hr as home_runs
from batting where yearid = 2002
group by playerid,home_runs,yearid 
order by home_runs desc 
limit 1;

--2. Which team spent the most/least money on player salaries in 2002?
select * 
from salaries;

select *
from teams t ;
--Which team spent the most
select teamid,sum(salary)
from salaries where yearid =2002
group by teamid 
order by sum(salary) desc 
limit 1;
--Which team spent the least
select teamid,sum(salary)
from salaries where yearid =2002
group by teamid 
order by sum(salary) asc  
limit 1;

--3. Which player averaged the fewest at bats between home runs in 2002?
select *
from batting b ;

select playerid,avg(ab),hr
from batting where yearid=2002 and hr>0
group by playerid ,hr
order by avg(ab) desc 
limit 1;







