# Write your MySQL query statement below
with cte as (
select question_id, count(question_id) bot, count(answer_id) top 
from SurveyLog
group by question_id) 

select question_id survey_log
from cte 
where top / bot = (select max(top / bot) from cte)
order by question_id 
limit 1