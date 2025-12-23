import pandas as pd
print(pd.__version__)

customers_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_customers_dataset.csv", low_memory=False)

customers = pd.DataFrame(
    {
        "customer_id": customers_df["customer_id"],
        "customer_unique_id": customers_df["customer_unique_id"],
        "customer_zip_code_prefix": customers_df["customer_zip_code_prefix"],
        "customer_city": customers_df["customer_city"],
        "customer_state": customers_df["customer_state"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

customers.to_csv("customers.csv", index=False)

#print(customers)
