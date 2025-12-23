import mysql.connector
import pandas as pd

# print(mysql.connector.__version__)
# print(pd.__version__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="olist_sales_analysis"
)
cursor = connection.cursor()

customers_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\customers.csv")

for _, row in customers_data.iterrows():
    cursor.execute(
        """
        INSERT INTO customers
        (customer_id, customer_unique_id,
        customer_zip_code_prefix, customer_city, customer_state)
        VALUES (%s, %s, %s, %s, %s)
        """,
        (
            row["customer_id"],
            row["customer_unique_id"],
            int(row["customer_zip_code_prefix"]),
            row["customer_city"],
            row["customer_state"]
        )
    )

connection.commit()
