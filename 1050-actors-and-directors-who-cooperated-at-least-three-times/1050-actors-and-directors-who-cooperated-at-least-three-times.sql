# Write your MySQL query statement below
SELECT actor_id, director_id
FROM ActorDirector a
GROUP BY a.actor_id, a.director_id
HAVING COUNT(*) >= 3