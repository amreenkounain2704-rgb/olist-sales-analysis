import mysql.connector
import pandas as pd

print(mysql.connector.__version__)
print(pd.__version__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="olist_sales_analysis"
)
cursor = connection.cursor()

orders_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\orders.csv")

for _, row in orders_data.iterrows():
    cursor.execute(
        """
        INSERT INTO orders
        (order_id,
        customer_id,
        order_status,
        order_purchase_timestamp,
        order_approved_at,
        order_delivered_carrier_date,
        order_delivered_customer_date,
        order_estimated_delivery_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["order_id"],
            row["customer_id"],
            row["order_status"],
            row["order_purchase_timestamp"],
            row["order_approved_at"],
            row["order_delivered_carrier_date"],
            row["order_delivered_customer_date"],
            row["order_estimated_delivery_date"]
        )
    )

connection.commit()
