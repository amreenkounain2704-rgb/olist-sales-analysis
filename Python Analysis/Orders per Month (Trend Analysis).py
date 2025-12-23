import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

orders = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\orders.csv")

orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

orders["month"] = orders["order_purchase_timestamp"].dt.to_period("M")

monthly_orders = orders.groupby("month")["order_id"].count()

plt.figure(figsize = (8,5))
plt.plot(monthly_orders.index.astype(str), monthly_orders.values)
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Number of Orders")
plt.xticks(rotation = 45)
plt.show()

