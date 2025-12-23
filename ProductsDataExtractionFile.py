import pandas as pd
print(pd.__version__)

products_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_products_dataset.csv", low_memory=False)

products = pd.DataFrame(
    {
        "product_id": products_df["product_id"],
        "product_category_name": products_df["product_category_name"],
        "product_name_length": products_df["product_name_length"],
        "product_description_length": products_df["product_description_length"],
        "product_photos_qty": products_df["product_photos_qty"],
        "product_weight_g": products_df["product_weight_g"],
        "product_length_cm": products_df["product_length_cm"],
        "product_height_cm": products_df["product_height_cm"],
        "product_width_cm": products_df["product_width_cm"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

products.to_csv("products.csv", index=False)

#print(products)
