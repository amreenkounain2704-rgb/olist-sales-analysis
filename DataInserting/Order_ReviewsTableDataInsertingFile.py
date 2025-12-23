import mysql.connector
import pandas as pd

print(mysql.connector.__version__)
print(pd.__version__)

df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\order_reviews.csv")

df["review_creation_date"] = pd.to_datetime(
    df["review_creation_date"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

df["review_answer_timestamp"] = pd.to_datetime(
    df["review_answer_timestamp"],
    format="%d-%m-%Y %H:%M",
    errors="coerce"
)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="olist_sales_analysis"
)

cursor = connection.cursor()

insert_query ="""
INSERT INTO order_reviews (
    review_id,
    order_id,
    review_score,
    review_comment_title,
    review_comment_message,
    review_creation_date,
    review_answer_timestamp
)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

for _,row in df.iterrows():
    cursor.execute(insert_query, (
            row["review_id"],
            row["order_id"],
            int(row["review_score"]),
            row["review_comment_title"],
            row["review_comment_message"],
            row["review_creation_date"],
            row["review_answer_timestamp"]
        )
    )

connection.commit()
