import pandas as pd
from datetime import datetime

from get_product_info import (get_product_categories, get_products_info)

from cookie import (cookie_token)

brands_list = [
    #{"id": "b_arceup81f2", "name": "Latico Leathers"}, 
     #          {"id": "b_6dyd8buw9c", "name": "Sarta"}, 
               #{"id": "b_40j19ly1ct", "name": "Roma Leathers (Top Shop)"}, 
               #{"id": "b_b2pjelg0sv", "name": "Sixtease Bags USA"}, 
               {"id": "b_aikxxfpecb", "name": "Threaded Pair"}]

# we loop over the different brands and get the products info
for brand in brands_list:
    products_info = get_products_info(brand_token=brand["id"], cookie=cookie_token)

    # Get the current date in yyyy/mm/dd format
    current_date = datetime.now().strftime('%Y%m%d')

    # Create the file name with the current date
    file_name = f'{brand["name"]}_products_{current_date}.csv'

    # Create a dataframe from the extracted information
    df = pd.DataFrame(products_info)
    df.to_csv(file_name, index=False)

