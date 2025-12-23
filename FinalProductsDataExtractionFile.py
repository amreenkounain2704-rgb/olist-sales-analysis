import pandas as pd
print(pd.__version__)

# Read original products dataset

products = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_products_dataset.csv", low_memory=False)

# Read translation file

translation = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\product_category_name_translation.csv", low_memory=False)

# Keep only needed columns from translation

translation = translation[
    ["product_category_name","product_category_name_english"]
]

# MAP English category into products

products = products.merge(
    translation,
    on="product_category_name",
    how="left"
)

# Remove duplicates

products = products.dropna().drop_duplicates().reset_index(drop=True)

# Save ONE final products file

products.to_csv(
"D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\products.csv", index=False)

#print(products)