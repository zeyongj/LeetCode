# Write your MySQL query statement below
SELECT
  CASE
    WHEN mod(id, 2) = 1 AND id = max_id THEN id 
    WHEN mod(id, 2) = 1 THEN id + 1
    ELSE id - 1
  END AS id, student
FROM (
  SELECT *, MAX(id) OVER() as max_id 
  FROM Seat
) AS data
ORDER BY id ASC;
