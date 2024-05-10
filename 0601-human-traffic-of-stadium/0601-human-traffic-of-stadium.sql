# Write your MySQL query statement below
WITH Flagged AS (
    SELECT 
        id,
        visit_date,
        people,
        CASE 
            WHEN people >= 100 THEN 1 
            ELSE 0 
        END as is_valid
    FROM Stadium
),
Labeled AS (
    SELECT
        *,
        SUM(is_valid) OVER (ORDER BY id) as cumulative_sum
    FROM Flagged
),
Grouped AS (
    SELECT
        *,
        id - ROW_NUMBER() OVER (ORDER BY id) as group_id
    FROM Labeled
    WHERE is_valid = 1
),
Counted AS (
    SELECT
        group_id,
        COUNT(*) as cnt
    FROM Grouped
    GROUP BY group_id
    HAVING COUNT(*) >= 3
)
SELECT 
    S.id,
    S.visit_date,
    S.people
FROM Stadium S
JOIN Grouped G ON S.id = G.id
JOIN Counted C ON G.group_id = C.group_id
ORDER BY S.visit_date;

