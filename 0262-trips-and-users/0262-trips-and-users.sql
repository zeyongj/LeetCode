# Write your MySQL query statement below
select 
a.Request_at as Day,
round(count(case when Status <> "completed" then Id else null end)/count(Id),2) as `Cancellation Rate`
from (
select 
	a.Id, a.Client_Id, a.Driver_Id, a.City_Id, a.Status, a.Request_at
from Trips a
join Users b on a.Client_Id = b.Users_Id and b.Banned = "No" and b.Role = "client"
join Users c on a.Driver_Id = c.Users_Id and c.Banned = "No" and c.Role = "driver"
where a.Request_at >= "2013-10-01"
and a.Request_at <= "2013-10-03"
) a
group by a.Request_at
;