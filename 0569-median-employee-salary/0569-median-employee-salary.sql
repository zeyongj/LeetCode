# Write your MySQL query statement below
WITH cte AS (
SELECT 
	id,
	company,
	Salary,
	ROW_NUMBER() OVER(PARTITION BY company ORDER BY Salary) as rn,
	COUNT(*) OVER(PARTITION BY company ) as rc 
FROM Employee
)

SELECT Id, company, salary 
FROM cte 
WHERE rn IN ( (rc+1 ) DIV 2 , (rc+2) DIV 2 )