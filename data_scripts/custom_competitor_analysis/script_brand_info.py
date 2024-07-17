import pandas as pd

from get_competitors_brand_info import (get_all_competitors_brand_data)

# brand_owner = "Boredwalk"
# brand_owner = "Glimmer Wish"
#brand_owner = "Trek Light"
# brand_owner = "Couleur Nature"
#brand_owner = "Little Hometown"
# brand_owner = "Be Huppy"
# brand_owner = "Grab2art"
# brand_owner = "Cheese Brothers"
# brand_owner = "Teleties"
# brand_owner = "Tushy"
# brand_owner = "Medify"
#brand_owner = "Future Kind"
# brand_owner = "Jack Archer"
brand_owner = "Dolan Geiman"

brands_data = get_all_competitors_brand_data(brand_owner)

df = pd.DataFrame(brands_data)

df.to_csv("brand_info.csv", index=False)

# we create a csv file with the brand info
#df.to_csv(f"../../dashboard/dashboard_data/{brand_owner.lower().replace(' ', '_')}/competitors_data/custom_brand_info.csv", index=False)

