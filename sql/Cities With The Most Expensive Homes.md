Write a query that identifies cities with higher than average home prices when compared to the national average. Output the city names.

zillow_transactions

id:
int
state:
varchar
city:
varchar
street_address:
varchar
mkt_price:
int

```sql

select city 
from zillow_transactions
group by city
having avg(mkt_price) > (select avg(mkt_price) from zillow_transactions)

```