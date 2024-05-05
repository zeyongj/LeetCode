# Write your MySQL query statement below
SELECT x, y, z, 
    CASE
        WHEN t.x + t.y > t.z AND t.x + t.z > t.y AND t.z + t.y > t.x THEN "Yes"
        ELSE "No"
    END AS triangle
FROM Triangle t