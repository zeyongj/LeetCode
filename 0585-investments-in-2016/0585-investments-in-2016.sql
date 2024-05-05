# Write your MySQL query statement below
WITH DuplicateTIV AS (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(pid) > 1
),
UniqueCities AS (
    SELECT pid, tiv_2015, tiv_2016
    FROM Insurance
    WHERE (lat, lon) IN (
        SELECT lat, lon
        FROM Insurance
        GROUP BY lat, lon
        HAVING COUNT(pid) = 1
    )
),
ValidPolicies AS (
    SELECT i.pid, i.tiv_2016
    FROM Insurance i
    JOIN DuplicateTIV d ON i.tiv_2015 = d.tiv_2015
    JOIN UniqueCities u ON i.pid = u.pid
)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM ValidPolicies;
