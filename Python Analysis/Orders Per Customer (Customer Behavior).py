import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

orders = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DataExtractionFiles\\orders.csv")

orders_per_customer = orders.groupby("customer_id")["order_id"].count()

plt.figure(figsize = (8,5))
plt.hist(orders_per_customer,bins = 20)
plt.title("Orders per Customer")
plt.xlabel("Number of Orders")
plt.ylabel("Customers")
plt.show()
