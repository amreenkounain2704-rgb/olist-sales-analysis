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

products_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\products.csv")

for _, row in products_data.iterrows():
    cursor.execute(
        """
        INSERT INTO products
        (product_id,
        product_category_name,
        product_category_name_english,
        product_name_length,
        product_description_length,
        product_photos_qty,
        product_weight_g,
        product_length_cm,
        product_height_cm,
        product_width_cm)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["product_id"],
            row["product_category_name"],
            row["product_category_name_english"],
            int(row["product_name_length"]),
            int(row["product_description_length"]),
            int(row["product_photos_qty"]),
            int(row["product_weight_g"]),
            int(row["product_length_cm"]),
            int(row["product_height_cm"]),
            int(row["product_width_cm"])
        )
    )

connection.commit()

