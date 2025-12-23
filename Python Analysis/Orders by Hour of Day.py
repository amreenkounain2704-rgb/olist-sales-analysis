import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

orders = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\orders.csv")

orders["order_purchase_timestamp"] = pd.to_datetime(orders["order_purchase_timestamp"])

orders["hour"] = orders["order_purchase_timestamp"].dt.hour

orders.groupby("hour")["order_id"].count().plot()

plt.title("Orders by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Number of Orders")
plt.show()

