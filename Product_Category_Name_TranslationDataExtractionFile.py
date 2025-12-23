import pandas as pd
print(pd.__version__)

product_category_name_translation_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\product_category_name_translation.csv", low_memory=False)

product_category_name = pd.DataFrame(
    {
        "product_category_name": product_category_name_translation_df["product_category_name"],
        "product_category_name_english": product_category_name_translation_df["product_category_name_english"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

product_category_name.to_csv("product_category_name.csv", index=False)

product_category_name.to_csv("product_category_name.csv", index=False)

#print(product_category_name)
