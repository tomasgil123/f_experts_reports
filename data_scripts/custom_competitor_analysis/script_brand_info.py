import pandas as pd

from get_competitors_brand_info import (get_all_competitors_brand_data)

brand_owner = "Boredwalk"

brands_data = get_all_competitors_brand_data(brand_owner)

df = pd.DataFrame(brands_data)

# we create a csv file with the brand info
df.to_csv(f"../../dashboard/dashboard_data/{brand_owner.lower().replace(' ', '_')}/competitors_data/custom_brand_info.csv", index=False)