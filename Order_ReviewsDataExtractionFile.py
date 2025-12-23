import pandas as pd
print(pd.__version__)

order_reviews_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_order_reviews_dataset.csv", low_memory=False)

order_reviews = pd.DataFrame(
    {
        "review_id": order_reviews_df["review_id"],
        "order_id": order_reviews_df["order_id"],
        "review_score": order_reviews_df["review_score"],
        "review_comment_title": order_reviews_df["review_comment_title"],
        "review_comment_message": order_reviews_df["review_comment_message"],
        "review_creation_date": order_reviews_df["review_creation_date"],
        "review_answer_timestamp": order_reviews_df["review_answer_timestamp"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

order_reviews.to_csv("order_reviews.csv", index=False)

#print(order_reviews)



