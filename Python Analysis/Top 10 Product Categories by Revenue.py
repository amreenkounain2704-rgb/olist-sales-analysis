import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

order_items = pd.read_csv(
    "D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\order_items.csv"
)

products = pd.read_csv(
    "D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\products.csv"
)

sales_products = order_items.merge( products,on="product_id",how="left")

category_revenue = (
    sales_products
    .groupby("product_category_name_english")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure( figsize=(8,5))
category_revenue.plot(kind="bar")
plt.title("Top 10 Product Categories by Revenue")
plt.xlabel("Category")
plt.ylabel("Revenue")
plt.xticks(rotation = 45)
plt.show()
