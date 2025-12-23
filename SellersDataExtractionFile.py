import pandas as pd
print(pd.__version__)

sellers_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_sellers_dataset.csv", low_memory=False)

sellers = pd.DataFrame(
    {
       "seller_id":sellers_df["seller_id"],
        "seller_zip_code_prefix":sellers_df["seller_zip_code_prefix"],
        "seller_city":sellers_df["seller_city"],
        "seller_state":sellers_df["seller_state"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

sellers.to_csv("sellers.csv", index=False)

#print(sellers)
