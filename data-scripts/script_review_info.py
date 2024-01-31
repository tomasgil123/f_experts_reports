import pandas as pd
from datetime import datetime

from get_reviews_info import (get_reviews_info)

brands_list = [
    {"id": "b_arceup81f2", "name": "Latico Leathers"}, 
              {"id": "b_6dyd8buw9c", "name": "Sarta"}, 
               {"id": "b_40j19ly1ct", "name": "Roma Leathers (Top Shop)"}, 
               {"id": "b_b2pjelg0sv", "name": "Sixtease Bags USA"}, 
               {"id": "b_aikxxfpecb", "name": "Threaded Pair"}
               ]

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# we loop over the different brands and get the products info
for brand in brands_list:
    reviews_info = get_reviews_info(brand_token=brand["id"])

    print(reviews_info)
    # Create the file name with the current date
    file_name = f'{brand["name"]}_reviews.csv'

    # Create a dataframe from the extracted information
    df = pd.DataFrame(reviews_info)
    df['brand'] = brand["name"]
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# create csv based on the merged data
merged_data.to_csv('reviews.csv', index=False)