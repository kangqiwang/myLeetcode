Number Of Units Per Nationality

Find the number of apartments per nationality that are owned by people under 30 years old.

Output the nationality along with the number of apartments.

Sort records by the apartments count in descending order.

Tables: airbnb_hosts, airbnb_units

airbnb_hosts

host_id:
int
nationality:
varchar
gender:
varchar
age:
int


airbnb_units

host_id:
int

unit_id:
varchar
unit_type:
varchar

n_beds:
int
n_bedrooms:
int

country:
varchar

city:
varchar

```sql

select nationality, count(distinct unit_id)
from airbnb_units unit
JOIN airbnb_hosts host on unit.host_id=host.host_id
WHERE unit_type = 'Apartment' and age<30
group by nationality

```