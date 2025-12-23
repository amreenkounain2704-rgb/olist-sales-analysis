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

product_category_name_translation_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\product_category_name.csv")

for _, row in product_category_name_translation_data.iterrows():
    cursor.execute(
        """
        INSERT INTO product_category_name_translation
        (product_category_name,
        product_category_name_english)
        VALUES (%s, %s)
        """,
(
            row["product_category_name"],
            row["product_category_name_english"]
        )
    )

connection.commit()
