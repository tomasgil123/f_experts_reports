import os
import pandas as pd
from datetime import datetime

from get_product_info import (get_product_categories, get_products_info)

from cookie import (cookie_token)

brands_list = [
    {"id": "b_94de8w6es5", "name": "Tenzo Tea"}, 
              {"id": "b_doloeypc", "name": "Blume"}, 
               {"id": "b_8pbavjqbfx", "name": "Matcha & CO"}, 
               {"id": "b_4fvfm8f5", "name": "Dona"}, 
               {"id": "b_2wiwcytj", "name": "The Tea Spot"}]

# we loop over the different brands and get the products info
for brand in brands_list:
    products_info = get_products_info(brand_token=brand["id"], cookie=cookie_token)

    # Get the current date in yyyy/mm/dd format
    current_date = datetime.now().strftime('%Y%m%d')

    # Create the file name with the current date
    file_name = f'{brand["name"]}_products_{current_date}.csv'

    # Create a dataframe from the extracted information
    df = pd.DataFrame(products_info)
    df["brand"] = brand["name"]
    df.to_csv(file_name, index=False)


# we merged the csv generated
csv_directory = './'
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]
merged_data = pd.DataFrame()

for csv_file in csv_files:
    file_path = os.path.join(csv_directory, csv_file)
    df = pd.read_csv(file_path)
    merged_data = pd.concat([merged_data, df], ignore_index=True)
    # we create a new csv
    # Get the current date in yyyy/mm/dd format
    current_date = datetime.now().strftime('%Y%m%d')
    merged_data.to_csv(f"products_{current_date}.csv", index=False)
