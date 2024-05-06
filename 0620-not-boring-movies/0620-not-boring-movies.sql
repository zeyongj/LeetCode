# Write your MySQL query statement below
SELECT id, movie, description, rating
FROM Cinema c
WHERE c.id % 2 != 0 AND c.description != "boring" 
ORDER BY c.rating DESC