CREATE DATABASE olist_sales_analysis;

USE olist_sales_analysis;

CREATE TABLE customers(
customer_id VARCHAR(100) PRIMARY KEY,
customer_unique_id VARCHAR(200),
customer_zip_code_prefix INT,
customer_city VARCHAR(100),
customer_state VARCHAR(100)
);

SELECT * FROM olist_sales_analysis.customers;

CREATE TABLE geolocation(
geolocation_id INT AUTO_INCREMENT PRIMARY KEY,
geolocation_zip_code_prefix INT,
geolocation_lat DECIMAL,
geolocation_lng DECIMAL,
geolocation_city VARCHAR(100),
geolocation_state VARCHAR(100)
);

SELECT * FROM olist_sales_analysis.geolocation;

CREATE TABLE order_items(
order_id VARCHAR(100),
order_item_id INT,
product_id VARCHAR(100),
seller_id VARCHAR(100),
shipping_limit_date DATETIME,
price DECIMAL,
freight_value DECIMAL,
PRIMARY KEY (order_id, order_item_id)
);

SELECT * FROM olist_sales_analysis.order_items;

CREATE TABLE order_payments(
id_order INT AUTO_INCREMENT PRIMARY KEY,
order_id VARCHAR(100),
payment_sequential INT,
payment_type VARCHAR(50),
payment_installments INT,
payment_value DECIMAL
);

SELECT * FROM olist_sales_analysis.order_payments;

CREATE TABLE order_reviews(
id_review INT AUTO_INCREMENT PRIMARY KEY,
review_id VARCHAR(100),
order_id VARCHAR(100),
review_score INT,
review_comment_title VARCHAR(100),
review_comment_message VARCHAR(100),
review_creation_date DATE,
review_answer_timestamp DATETIME
);

SELECT * FROM olist_sales_analysis.order_reviews;

CREATE TABLE orders(
order_id VARCHAR(100) PRIMARY KEY,
customer_id VARCHAR(100),
order_status VARCHAR(100),
order_purchase_timestamp DATETIME,
order_approved_at DATETIME,
order_delivered_carrier_date DATETIME,
order_delivered_customer_date DATETIME,
order_estimated_delivery_date DATETIME
);

SELECT * FROM olist_sales_analysis.orders;

CREATE TABLE products(
product_id VARCHAR(100) PRIMARY KEY,
product_category_name VARCHAR(100),
product_category_name_english VARCHAR(100),
product_name_length INT,
product_description_length INT,
product_photos_qty INT,
product_weight_g INT,
product_length_cm INT,
product_height_cm INT,
product_width_cm int
);

SELECT * FROM olist_sales_analysis.products;

CREATE TABLE sellers(
seller_id VARCHAR(100) PRIMARY KEY,
seller_zip_code_prefix INT,
seller_city VARCHAR (100),
seller_state VARCHAR(100)
);

SELECT * FROM olist_sales_analysis.sellers;

CREATE TABLE product_category_name_translation(
product_category_name VARCHAR(100) PRIMARY KEY,
product_category_name_english VARCHAR(100) 
);

SELECT * FROM olist_sales_analysis.product_category_name_translation;

USE olist_sales_analysis;

ALTER TABLE orders
ADD CONSTRAINT 
fk_orders_customer_id
FOREIGN KEY (customer_id) 
REFERENCES customers(customer_id);
    
ALTER TABLE order_items
ADD CONSTRAINT
fk_order_items_order_id
FOREIGN KEY (order_id) 
REFERENCES orders (order_id);

ALTER TABLE order_items
ADD CONSTRAINT 
fk_order_items_product_id
FOREIGN KEY (product_id) 
REFERENCES products (product_id);
    
ALTER TABLE order_items
ADD CONSTRAINT
fk_order_items_seller_id
FOREIGN KEY (seller_id) 
REFERENCES sellers (seller_id);
        
ALTER TABLE order_reviews
ADD CONSTRAINT 
fk_order_reviews_order_id
FOREIGN KEY (order_id) 
REFERENCES orders (order_id);

ALTER TABLE order_payments
ADD CONSTRAINT
fk_order_payments_order_id
FOREIGN KEY (order_id)
REFERENCES orders (order_id);
    
SET FOREIGN_KEY_CHECKS = 0;

SET FOREIGN_KEY_CHECKS = 1;

-- Increasing varchar range

ALTER TABLE order_reviews
MODIFY review_comment_message MEDIUMTEXT;

