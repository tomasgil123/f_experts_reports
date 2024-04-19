import pandas as pd
from datetime import datetime

from get_product_info_custom import (get_products_info)

# brand_owner = "Boredwalk"
#brand_owner = "Glimmer Wish"
brand_owner = "Couleur Nature"

data = get_products_info(brand_owner)

# we convert data to a dataframe
df = pd.DataFrame(data)

# Get the current date in yyyy/mm/dd format
current_date = datetime.now().strftime('%Y-%m-%d')
# we create a csv file with the collections info
#df.to_csv(f"../../dashboard/dashboard_data/{brand_owner.lower().replace(' ', '_')}/competitors_data/custom_products_{current_date}.csv", index=False)

df.to_csv("products_info.csv", index=False)

