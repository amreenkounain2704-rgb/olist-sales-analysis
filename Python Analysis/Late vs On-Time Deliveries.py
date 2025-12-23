import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

orders = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\orders.csv")

late_orders = orders[
    orders["order_delivered_customer_date"] >
    orders["order_estimated_delivery_date"]
]

on_time = len(orders) - len(late_orders)

plt.figure(figsize=(6,4))
plt.bar(["On Time", "Late"], [on_time, len(late_orders)])
plt.title("Delivery Performance")
plt.ylabel("Number of Orders")
plt.show()