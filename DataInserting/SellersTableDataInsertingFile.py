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

sellers_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\sellers.csv")

for _, row in sellers_data.iterrows():
    cursor.execute(
        """
        INSERT INTO sellers
        (seller_id,
        seller_zip_code_prefix,
        seller_city,
        seller_state)
        VALUES (%s, %s, %s, %s)
        """,
        (
            row["seller_id"],
            int(row["seller_zip_code_prefix"]),
            row["seller_city"],
            row["seller_state"]
        )
    )

connection.commit()
