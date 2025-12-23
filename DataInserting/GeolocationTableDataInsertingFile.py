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

geolocation_data = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\geolocation.csv")

for _, row in geolocation_data.iterrows():
    cursor.execute(
        """
        INSERT INTO geolocation
        (geolocation_zip_code_prefix,
        geolocation_lat,
        geolocation_lng, 
        geolocation_city, 
        geolocation_state)
        VALUES (%s, %s, %s, %s, %s)
        """,
    (
            int(row["geolocation_zip_code_prefix"]),
            float(row["geolocation_lat"]),
            float(row["geolocation_lng"]),
            row["geolocation_city"],
            row["geolocation_state"]
           )
    )

connection.commit()
