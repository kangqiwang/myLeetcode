Redfin helps clients to find agents. Each client will have a unique request_id and each request_id has several calls. For each request_id, the first call is an “initial call” and all the following calls are “update calls”.  What's the average call duration for all update calls?

redfin_call_tracking

created_on:
datetime
request_id:
int
call_duration:
int
id:
int


```sql
select avg(call_duration)
from redfin_call_tracking
where id in
(select id
from
    (SELECT *,
               rank() OVER (PARTITION BY request_id
                            ORDER BY created_on) AS rk
        FROM redfin_call_tracking) sq
    where rk >1
    )
```


```python
first_call = redfin_call_tracking.groupby(["request_id"])["id"].min()
result=redfin_call_tracking[~redfin_call_tracking["id"].isin(first_call)]["call_duration"].mean()

```