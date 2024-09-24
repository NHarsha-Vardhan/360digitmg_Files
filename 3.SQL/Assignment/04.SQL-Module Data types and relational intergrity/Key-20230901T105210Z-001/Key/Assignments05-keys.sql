# Q 1)
/*Create a database with a sales table containing data types like int, varchar, char ,date, time, timestamp, Boolean, decimal, text ?
*/

create database sales_dtype;

use sales_dtype;

CREATE TABLE sales_dtype (
  order_id INT,
  product_name VARCHAR(50),
  customer_name CHAR(50),
  order_date DATE,
  ship_time TIME,
  order_timestamp TIMESTAMP,
  is_returned BOOLEAN,
  sales_total DECIMAL(10, 2),
  order_notes TEXT
);


# Q 2)
/*Insert 10 random values in the table ?
*/
INSERT INTO sales_dtype (order_id, product_name, customer_name, order_date, ship_time, order_timestamp, is_returned, sales_total, order_notes)
VALUES
  (1001, 'Product A', 'John Smith', '2023-04-11', '14:30:00', '2023-04-11 14:30:00', FALSE, 49.99, 'Order notes for Product A'),
  (1002, 'Product B', 'Sara Johnson', '2023-04-11', '15:00:00', '2023-04-11 15:00:00', FALSE, 99.99, 'Order notes for Product B'),
  (1003, 'Product C', 'Michael Davis', '2023-04-12', '10:30:00', '2023-04-12 10:30:00', FALSE, 149.99, 'Order notes for Product C'),
  (1004, 'Product D', 'Emily Anderson', '2023-04-13', '13:45:00', '2023-04-13 13:45:00', TRUE, 199.99, 'Order notes for Product D'),
  (1005, 'Product E', 'Daniel Rodriguez', '2023-04-14', '16:20:00', '2023-04-14 16:20:00', FALSE, 249.99, 'Order notes for Product E'),
  (1006, 'Product F', 'Jessica Williams', '2023-04-14', '18:15:00', '2023-04-14 18:15:00', FALSE, 299.99, 'Order notes for Product F'),
  (1007, 'Product G', 'David Brown', '2023-04-15', '11:00:00', '2023-04-15 11:00:00', FALSE, 349.99, 'Order notes for Product G'),
  (1008, 'Product H', 'Laura Perez', '2023-04-15', '14:30:00', '2023-04-15 14:30:00', TRUE, 399.99, 'Order notes for Product H'),
  (1009, 'Product I', 'Matthew Lee', '2023-04-16', '12:00:00', '2023-04-16 12:00:00', FALSE, 449.99, 'Order notes for Product I'),
  (1010, 'Product J', 'Julia Martinez', '2023-04-17', '9:15:00', '2023-04-17 09:15:00', FALSE, 499.99, 'Order notes for Product J');

# Q 3) 
/*Change the data type of the existing column from DECIMAL (10,2) to FLOAT ?
*/

ALTER TABLE sales_dtype
MODIFY COLUMN sales_total FLOAT;

# Q 4) 
/*Change the data type of the existing column from Text to Varchar?
Sol:
*/

ALTER TABLE sales_dtype
MODIFY COLUMN order_notes varchar(255);
