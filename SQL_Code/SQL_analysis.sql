-- olist sales analysis

-- 1. total number of orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- 2. Total Revenue
SELECT SUM(payment_value) AS total_revenue
FROM order_payments;

-- 3. Total Customers
SELECT COUNT(DISTINCT customer_id) AS total_customers
FROM customers;

-- 4. orders per customer
SELECT customer_id, COUNT(order_id) AS total_count
FROM orders
GROUP BY customer_id 
ORDER BY total_count DESC
LIMIT 0, 1000;

-- 5. monthly order counts
SELECT 
	DATE_FORMAT(order_purchase_timestamp, '%Y-%m') AS month,
    COUNT(order_id) AS total_orders
FROM orders
GROUP BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m')
ORDER BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m');

-- 6. monthly revenue
SELECT 
	DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS month,
    SUM(p.payment_value) AS revenue
FROM orders o
JOIN order_payments p ON o.order_id = p.order_id
GROUP BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m')
ORDER BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m');

-- 7. top 10 selling product categories
SELECT 
   p.product_category_name_english,
   COUNT(*) AS total_sold
FROM order_items oi
JOIN products p
    ON oi.product_id = p.product_id
GROUP BY p.product_category_name_english
ORDER BY total_sold DESC
LIMIT 10;

-- 8. revenue by product category
SELECT 
	p.product_category_name_english,
    SUM(oi.price) AS revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.product_category_name_english
ORDER BY revenue DESC;

-- 9. average order value
SELECT AVG(payment_value) AS avg_order_value
FROM order_payments;

-- 10. orders by customer state 
SELECT 
	c.customer_state,
    COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_state
ORDER BY total_orders DESC;

-- 11. average delivery time(days)
SELECT 
	AVG(DATEDIFF(order_delivered_customer_date,
				order_purchase_timestamp)) AS avg_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;

-- 12. late deliveries count
SELECT COUNT(*) AS late_orders
FROM orders
WHERE order_delivered_customer_date >
	  order_estimated_delivery_date;
      
-- 13. orders by payment type
SELECT payment_type, COUNT(*) AS total_orders
FROM order_payments
GROUP BY payment_type;

-- 14. average review score
SELECT AVG(review_score) AS avg_rating
FROM order_reviews;

-- 15. top 10 sellers by revenue
SELECT
    seller_id,
    SUM(price) AS total_revenue
FROM order_items
GROUP BY seller_id
ORDER BY total_revenue DESC
LIMIT 10;

