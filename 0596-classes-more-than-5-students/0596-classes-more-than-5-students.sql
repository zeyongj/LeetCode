# Write your MySQL query statement below
SELECT class
FROM courses c
GROUP BY c.class
HAVING COUNT(DISTINCT student) >= 5