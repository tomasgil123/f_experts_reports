import pandas as pd

from get_competitors_brand_info import (get_all_competitors_brand_data)

# brand_owner = "Boredwalk"
# brand_owner = "Glimmer Wish"
brand_owner = "Trek Light"
brands_data = get_all_competitors_brand_data(brand_owner)

df = pd.DataFrame(brands_data)

df.to_csv("brand_info.csv", index=False)

# we create a csv file with the brand info
#df.to_csv(f"../../dashboard/dashboard_data/{brand_owner.lower().replace(' ', '_')}/competitors_data/custom_brand_info.csv", index=False)

# df_brand_info = pd.read_csv("brand_info.csv")
# df_products_info = pd.read_csv("custom_products_2024-04-03.csv")

# # we merge df_brand_info (Brand Token column) into df_products_info (Brand ID column), we only want to append "Brand Name" column
# df_products_info = df_products_info.merge(df_brand_info[["Brand Token", "Brand Name"]], left_on="Brand ID", right_on="Brand Token", how="left")

# # we rename "Brand Name" column to "brand"
# df_products_info.rename(columns={"Brand Name": "brand"}, inplace=True)

# # we donwload it as a csv
# df_products_info.to_csv("products_info.csv", index=False)