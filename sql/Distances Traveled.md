Find the top 10 users that have traveled the greatest distance. Output their id, name and a total distance traveled.

Tables: lyft_rides_log, lyft_users

lyft_rides_log


id:
int
user_id:
int
distance:
int

lyft_users

id:
int
name:
varchar


```sql

select user_id ,sum(distance) as total,name
from lyft_rides_log lrl
join lyft_users lu on lrl.user_id=lu.id
group by user_id,name
order by total desc
limit 10


```