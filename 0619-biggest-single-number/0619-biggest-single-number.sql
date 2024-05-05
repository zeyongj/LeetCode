# Write your MySQL query statement below
SELECT MAX(num) as num
FROM
    (SELECT num
     FROM MyNumbers m
     GROUP BY m.num
     HAVING COUNT(m.num) = 1
    )
AS SingleNumbers