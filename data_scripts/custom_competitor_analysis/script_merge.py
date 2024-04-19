import pandas as pd
from datetime import datetime
import glob

brand_owner = "Couleur Nature"

df_brand_info = pd.read_csv("brand_info.csv")

products_info = glob.glob(f"custom_products_*.csv")

df_products_info = pd.read_csv(products_info[0])

# we merge df_brand_info (Brand Token column) into df_products_info (Brand ID column), we only want to append "Brand Name" column
df_products_info = df_products_info.merge(df_brand_info[["Brand Token", "Brand Name"]], left_on="Brand ID", right_on="Brand Token", how="left")

# we rename "Brand Name" column to "brand"
df_products_info.rename(columns={"Brand Name": "brand"}, inplace=True)

# we donwload it as a csv
#df_products_info.to_csv("products_info.csv", index=False)

# Get the current date in yyyy/mm/dd format
current_date = datetime.now().strftime('%Y-%m-%d')

df_products_info.to_csv(f"../../dashboard/dashboard_data/{brand_owner.lower().replace(' ', '_')}/competitors_data/custom_products_{current_date}.csv", index=False)
