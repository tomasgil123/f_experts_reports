import pandas as pd
from datetime import datetime
import time

from get_reviews_info import (get_reviews_info)

# we create a dataframe using the brands_competitors csv
df_brands = pd.read_csv('brands_competitors.csv')

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
# brand_owners = ['Tushy']
# brand_owners = ['Medify']
# brand_owners = ['Future Kind']
# brand_owners = ['Jack Archer']
# brand_owners = ['Dolan Geiman']
#brand_owners = ['Viori']
#brand_owners = ['Levtex Home']
brand_owners = ['Tagua']

# we iterate over the brand_owners
for brand_owner in brand_owners:
    # we filter the dataframe to get the brands for each brand_owner
    df_brands_filtered = df_brands[df_brands['brand_owner'] == brand_owner]
    # we get the brands list
    brands_list = df_brands_filtered.to_dict('records')

    # Create an empty DataFrame to store the merged data
    merged_data = pd.DataFrame()

    # we loop over the different brands and get the products info
    for brand in brands_list:
        reviews_info = get_reviews_info(brand_token=brand["id"])

        # Create a dataframe from the extracted information
        df = pd.DataFrame(reviews_info)
        df['brand'] = brand["name"]
        merged_data = pd.concat([merged_data, df], ignore_index=True)
        time.sleep(20)

    # create csv based on the merged data
    merged_data.to_csv(f"../dashboard/dashboard_data/{brand_owners[0].lower().replace(' ', '_')}/competitors_data/reviews.csv", index=False)