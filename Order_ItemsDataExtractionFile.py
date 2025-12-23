import pandas as pd
print(pd.__version__)

order_items = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_order_items_dataset.csv", low_memory=False)

order_items = pd.DataFrame(
    {
        "order_id": order_items["order_id"],
        "order_item_id": order_items["order_item_id"],
        "product_id": order_items["product_id"],
        "seller_id": order_items["seller_id"],
        "shipping_limit_date": order_items["shipping_limit_date"],
        "price": order_items["price"],
        "freight_value": order_items["freight_value"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

order_items.to_csv("order_items.csv", index=False)

#print(order_items)

