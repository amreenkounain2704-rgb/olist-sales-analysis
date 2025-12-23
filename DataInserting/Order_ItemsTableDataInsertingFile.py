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

order_items_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\order_items.csv")

for _, row in order_items_data.iterrows():
    cursor.execute(
        """
        INSERT INTO order_items 
        (order_id,
        order_item_id,
        product_id,
        seller_id,
        shipping_limit_date,
        price,
        freight_value)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["order_id"],
            int(row["order_item_id"]),
            row["product_id"],
            row["seller_id"],
            row["shipping_limit_date"],
            float(row["price"]),
            float(row["freight_value"]),
        )
    )

connection.commit()
