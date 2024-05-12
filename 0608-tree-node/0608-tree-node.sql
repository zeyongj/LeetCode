# Write your MySQL query statement below
SELECT t.id, 
    CASE
        WHEN t.p_id is null THEN "Root"
        WHEN t.id IN 
            (SELECT p_id 
             FROM Tree 
             WHERE p_id IS NOT NULL) THEN "Inner"
        ELSE "Leaf"
    END AS type
FROM Tree t