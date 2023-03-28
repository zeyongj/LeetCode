# Write your MySQL query statement below
select
    Employee.name, Bonus.bonus
from
    Employee left join
    Bonus on Employee.empid = Bonus.empid
where
    bonus < 1000 OR bonus IS NULL
;