import pandas as pd
print(pd.__version__)

geolocation_df = pd.read_csv("D:\\Data Analyst Course Classes\\FINAL PROJECT olist_sales_analysis\\DATASET\\olist_geolocation_dataset.csv", low_memory=False)


geolocation = pd.DataFrame(
    {
        "geolocation_zip_code_prefix": geolocation_df["geolocation_zip_code_prefix"],
        "geolocation_lat": geolocation_df["geolocation_lat"],
        "geolocation_lng": geolocation_df["geolocation_lng"],
        "geolocation_city": geolocation_df["geolocation_city"],
        "geolocation_state": geolocation_df["geolocation_state"]
    }
).dropna().drop_duplicates().reset_index(drop=True)

geolocation.to_csv("geolocation.csv", index=False)

#print(geolocation.head())


