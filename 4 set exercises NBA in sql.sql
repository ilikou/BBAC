--1.a Find all allstar MVP players.
select *
from allstar_mvps;

select *
from players ;

select allstar_mvps.player_id ,players."name"
from players inner join allstar_mvps 
on allstar_mvps.player_id=players.id;

--1.b Find all players born in New York.
select  "name", birth_place
from players where birth_place ilike '%New%York%';


--1.c Which players born in New York hold a MVP title?
select players."name",players.birth_place 
from players 
inner join allstar_mvps on players.id=allstar_mvps.player_id where  birth_place ilike '%New%York%';

--2. Which players have the same height?
select distinct players."name",players."height"
from players where "height"="height"
order by "height" desc ;

--3. List the top 10 of the players having the most Player of the Month Awards.
select distinct players."name",count(monthly_player_awards.award_type) as  count_player_of_month
from players inner join monthly_player_awards 
on monthly_player_awards.player_id =players."id"
group by "name"
order by count_player_of_month desc
limit 10;

--4. Using table teams, create a new column that writes the messages "More than 2000 wins",
-- "2000 wins" or "Less than 2000 wins" depending the number of wins it has,
-- and also print the name and the number of wins for each team.

select*
from teams ;

select short_name,total_wins, case
  when total_wins  > 2000 then 'More than 2000 wins'
  when total_wins  = 2000 then '2000 wins' else 'Less than 2000 wins'
end as wins_fact
from teams
group by short_name ,total_wins 
order by total_wins desc ;

--5.a  Create a view with the team id, team name and number of championships.
create view  teams_id_name_championships as select team_id,team_name,champions
from teams ;

select *
from teams_id_name_championships;

--5.b Print from the view all the teams from Miami or Milwaukee that have a championship.
select team_name,champions
from teams_id_name_championships where (team_name like '%Miami%' or  team_name like '%Milwaukee%') and champions > 0-- champions !=0
group by team_name,champions
order by team_name;

--5.c Update view with total wins and total loses.
create or replace view teams_id_name_championships as select team_id,team_name,champions,total_wins,total_losses
from teams;



select * 
from teams_id_name_championships;

select *
from player_awards pa ;

--6. Find all players that have both awards and other awards and print the name of the award as well.
--select distinct players."name"
select players."name",player_awards.award,other_player_awards.award 
from players inner join player_awards on  player_awards.player_id=players.id 
            inner join other_player_awards on other_player_awards.payer_id =players.id 
group by players."name",player_awards.award,other_player_awards.award 
order by players."name"

