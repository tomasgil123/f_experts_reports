import pandas as pd
from datetime import datetime

from cookie import (cookie_token)
from get_collections import (get_collections_info_for_brand)

# we create a dataframe using the brands_competitors csv
df_brands = pd.read_csv('brands_competitors.csv')

# get array of values for column "brand_owner"
# brand_owners = df_brands['brand_owner'].unique()
# brand_owners = ["Latico Leathers"]
brand_owners = ["Free Planet"]

# we iterate over the brand_owners
for brand_owner in brand_owners:
    # we filter the dataframe to get the brands for each brand_owner
    df_brands_filtered = df_brands[df_brands['brand_owner'] == brand_owner]
    # we get the brands list
    brands_list = df_brands_filtered.to_dict('records')

    # Create an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # we iterate over the brands list
    for brand in brands_list:
        print("brand", brand)
        collections_info = get_collections_info_for_brand(brand_token=brand["id"], cookie=cookie_token)
        df = pd.DataFrame(collections_info)
        df['brand'] = brand["name"]
        merged_data = pd.concat([merged_data, df], ignore_index=True)
    
    # we create a csv file with the collections info
    merged_data.to_csv(f"collections_{brand_owner}.csv", index=False)