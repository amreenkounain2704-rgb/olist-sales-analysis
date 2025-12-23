import matplotlib
# print(matplotlib.__version__)
import pandas as pd
# print(pd.__version__)
import matplotlib.pyplot as plt

payments = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_order_payments_dataset.csv")

payments_counts = payments.groupby("payment_type")["order_id"].count()

plt.figure(figsize = (6,4))
payments_counts.plot(kind="bar")
plt.title("Payment Type Distribution")
plt.xlabel("Payment Type")
plt.ylabel("Number of Orders")
plt.xticks(rotation = 45, ha = "right")
plt.show()

