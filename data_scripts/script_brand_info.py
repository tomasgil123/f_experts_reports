import pandas as pd
from datetime import datetime

from cookie import (cookie_token)
from get_competitors_brand_info import (get_competitors_brand_data)

# we create a dataframe using the brands_competitors csv
df_brands = pd.read_csv('brands_competitors.csv')

# get array of values for column "brand_owner"
# brand_owners = df_brands['brand_owner'].unique()
# brand_owners = ["True Classic"]

# brand_owners = ["Little Hometown"]
# brand_owners = ["Be Huppy"]
# brand_owners = ["grab2art"]
# brand_owners = ['Cheese Brothers']
# brand_owners = ['Teleties']
# brand_owners = ['Tushy']
# brand_owners = ['Medify']
# brand_owners = ['Future Kind']
# brand_owners = ['Jack Archer']
brand_owners = ['Dolan Geiman']

# for each brand owner we get brand data
for brand_owner in brand_owners:
    # we filter the dataframe to get the brands for each brand_owner
    df_brands_filtered = df_brands[df_brands['brand_owner'] == brand_owner]
    # we get the brands list
    brands_list = df_brands_filtered.to_dict('records')
    brand_ids = df_brands_filtered['id'].unique()

    brands_data = get_competitors_brand_data(brand_ids)
    df = pd.DataFrame(brands_data)
    
    # we create a csv file with the brand info
    df.to_csv(f"../dashboard/dashboard_data/{brand_owners[0].lower().replace(' ', '_')}/brand_info.csv", index=False)