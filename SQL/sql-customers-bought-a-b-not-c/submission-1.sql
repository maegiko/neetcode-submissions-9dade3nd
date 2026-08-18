-- Write your query below
create or replace view purchasedAB(customer_id, customer_name)
as
select c.customer_id, c.customer_name
from customers c
join orders o on c.customer_id = o.customer_id
join orders o2 on c.customer_id = o2.customer_id
where o.product_name = 'A' and o2.product_name = 'B'
;

create or replace view purchasedC(customer_id, customer_name)
as
select c.customer_id, customer_name
from customers c
join orders o on c.customer_id = o.customer_id
where o.product_name = 'C'
;

select customer_id, customer_name 
from purchasedAB
except
(select * from purchasedC)
order by customer_name;