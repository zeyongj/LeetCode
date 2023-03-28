# Write your MySQL query statement below
with t as 
(select *, sum(frequency) over(order by num) Total_freq, 
 (sum(frequency) over())/2 median_num
from numbers)
           
select round(avg(num),1) as median
from t
where median_num between (Total_freq-frequency) and Total_freq