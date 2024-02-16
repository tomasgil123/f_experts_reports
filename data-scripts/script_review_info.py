import pandas as pd
from datetime import datetime

from get_reviews_info import (get_reviews_info)

brands_list = [
    {"id": "b_94de8w6es5", "name": "Tenzo Tea"}, 
               {"id": "b_doloeypc", "name": "Blume"}, 
               {"id": "b_8pbavjqbfx", "name": "Matcha & CO"}, 
                {"id": "b_4fvfm8f5", "name": "Dona"}, 
               {"id": "b_2wiwcytj", "name": "The Tea Spot"}
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