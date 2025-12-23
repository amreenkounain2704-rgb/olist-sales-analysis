import pandas as pd
#print(pd.__version__)

orders = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_orders_dataset.csv", low_memory=False)

orders = pd.DataFrame(
    {
        "order_id": orders["order_id"],
        "customer_id": orders["customer_id"],
        "order_status": orders["order_status"],
        "order_purchase_timestamp": orders["order_purchase_timestamp"],
        "order_approved_at": orders["order_approved_at"],
        "order_delivered_carrier_date": orders["order_delivered_carrier_date"],
        "order_delivered_customer_date":orders["order_delivered_customer_date"],
        "order_estimated_delivery_date": orders["order_estimated_delivery_date"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

orders.to_csv("orders.csv", index=False)

#print(orders)
