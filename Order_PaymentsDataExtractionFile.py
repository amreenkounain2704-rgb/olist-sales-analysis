import pandas as pd
print(pd.__version__)

order_payments_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_order_payments_dataset.csv", low_memory=False)

order_payments = pd.DataFrame(
    {
        "order_id": order_payments_df["order_id"],
        "payment_sequential": order_payments_df["payment_sequential"],
        "payment_type": order_payments_df["payment_type"],
        "payment_installments": order_payments_df["payment_installments"],
        "payment_value": order_payments_df["payment_value"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

order_payments.to_csv("order_payments.csv", index=False)

#print(order_payments)
