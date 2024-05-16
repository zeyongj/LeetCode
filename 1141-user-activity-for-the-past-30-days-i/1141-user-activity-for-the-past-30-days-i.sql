# Write your MySQL query statement below
SELECT a.activity_date AS day, COUNT(DISTINCT a.user_id) AS active_users
FROM Activity a
WHERE DATEDIFF('2019-07-27', a.activity_date) < 30 AND DATEDIFF('2019-07-27', a.activity_date)>=0
GROUP BY 1
