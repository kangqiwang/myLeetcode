Calculate the percentage of the total spend a customer spent on each order. Output the customer’s first name, order details, and percentage of the order cost to their total spend across all orders.


Assume each customer has a unique first name (i.e., there is only 1 customer named Karen in the dataset) and that customers place at most only 1 order a day.


Percentages should be represented as decimals



orders

id:
int
cust_id:
int
order_date:
datetime
order_details:
varchar
total_order_cost:
int


customers

id:
int
first_name:
varchar
last_name:
varchar
city:
varchar
address:
varchar
phone_number:
varchar


```sql

select first_name,order_details, total_order_cost/sum(total_order_cost) OVER (PARTITION BY c.id) as precentage_of_the_order_cost
from orders o
join customers c on o.cust_id=c.id

```