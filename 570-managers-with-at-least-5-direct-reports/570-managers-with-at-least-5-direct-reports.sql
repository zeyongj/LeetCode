# Write your MySQL query statement below
SELECT a.Name
FROM Employee a, Employee b
WHERE a.Id = b.ManagerId
GROUP BY b.ManagerId
HAVING COUNT(*) >= 5