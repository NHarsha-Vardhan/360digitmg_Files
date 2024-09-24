#1.	Run the below query to create the datasets.
#a.	/*retrieve sales table from the supermart_db (sales dataset contains multiple years data)*/

use supermart_db;
SELECT * FROM sales;

/* Counting the total number of rows in sales table */
SELECT COUNT(*) FROM sales;

describe sales;

#b. /* Counting the number of distinct customer_id values in sales table */
SELECT COUNT(DISTINCT customer_id) FROM sales;

### B.	/* Customers with ages between 20 and 60 */
          #•	create table customer_20_60 as select * from customer where age between 20 and 60;
          #•	select count (*) from customer_20_60;


/* Customers with ages between 20 and 60 */
CREATE TABLE customer_20_60 AS SELECT * FROM customers WHERE age BETWEEN 20 AND 60;
SELECT COUNT(*) FROM customer_20_60;


#2.	Find the total sales done in every state for customer_20_60 and sales table
#Hint: Use Joins and Group By command


SELECT c.state, SUM(s.sales)
FROM sales s
JOIN customer_20_60 c ON s.customer_id = c.customer_id
GROUP BY c.state;
describe products;

#3.	Get data containing Product_id, Product name, category, total sales value of that product, and total quantity sold. (Use sales and product tables)

SELECT p.product_id, p.product_name, p.sub_category, 
    SUM(s.sales) AS total_sales_value, 
    SUM(s.Quantity) AS total_quantity_sold
FROM sales s
JOIN products p ON s.product_id = p.product_id
GROUP BY p.product_id
