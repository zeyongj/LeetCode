# Write your MySQL query statement below
SELECT e.employee_id, e.department_id
FROM Employee e
WHERE e.primary_flag='Y' OR 
    e.employee_id IN(
        SELECT employee_id
        FROM Employee
        Group by employee_id
        having count(employee_id)=1)