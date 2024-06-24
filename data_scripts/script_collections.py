import pandas as pd
from datetime import datetime
import time

from cookie import (cookie_token)
from get_collections import (get_collections_info_for_brand)

# we create a dataframe using the brands_competitors csv
df_brands = pd.read_csv('brands_competitors.csv')

# get array of values for column "brand_owner"
# brand_owners = df_brands['brand_owner'].unique()
# brand_owners = ["Latico Leathers"]
# brand_owners = ["True Classic"]
# brand_owners = ["Glimmer Wish"]
# brand_owners = ["Trek Light"]
# brand_owners = ["Couleur Nature"]
# brand_owners = ["Little Hometown"]
# brand_owners = ["Be Huppy"]
# brand_owners = ["grab2art"]
# brand_owners = ['Cheese Brothers']
# brand_owners = ['Teleties']
brand_owners = ['Tushy']

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
        time.sleep(30)
    
    # we create a csv file with the collections info
    merged_data.to_csv(f"../dashboard/dashboard_data/{brand_owners[0].lower().replace(' ', '_')}/competitors_data/collections.csv", index=False)