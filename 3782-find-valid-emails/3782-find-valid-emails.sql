# Write your MySQL query statement below
SELECT user_id, email
FROM Users
WHERE email REGEXP '^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
ORDER BY user_id;