import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

payments = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_order_payments_dataset.csv")

avg_order_value = payments["payment_value"].mean()

plt.figure(figsize=(5,3))
plt.bar(["Average Order Value"],[avg_order_value])
plt.ylabel("Amount")
plt.title("Average Order Value")
plt.show()

