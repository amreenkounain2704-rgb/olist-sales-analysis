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

order_payments_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\order_payments.csv")

cursor.execute("SELECT order_id FROM orders")
valid_orders = set(row[0] for row in cursor.fetchall())

order_payments_data = order_payments_data[
    order_payments_data["order_id"].isin(valid_orders)
]

print(f"Rows afterfiltering: {len(order_payments_data)}")

insert_query = """
INSERT INTO order_payments 
(order_id, 
 payment_sequential,
 payment_type,
 payment_installments,
 payment_value)
VALUES (%s, %s, %s, %s, %s)
"""
for _, row in order_payments_data.iterrows():
    cursor.execute(insert_query, (
        row["order_id"],
        int(row["payment_sequential"]),
        row["payment_type"],
        int(row["payment_installments"]),
        float(row["payment_value"])
        )
    )

connection.commit()