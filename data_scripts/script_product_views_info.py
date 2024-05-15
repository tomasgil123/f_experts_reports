import pandas as pd
from get_product_views_info import (get_page_views_for_all_months_since_date)
from cookie import (cookie_token)

# brand_name = "true_classic"
# brand_name = "couleur_nature"
# brand_name = "caravan"
brand_name = "bon_artis"
# brand_name = "lothantique"
# brand_name = "shinesty"
# brand_name = "glimmer_wish"
# brand_name = "trek_light"
# brand_name = "latico_leathers"
# brand_name = "little_hometown"
# brand_name = "be_huppy"

data = get_page_views_for_all_months_since_date(cookie=cookie_token, starting_date="2023-01-01")

# we create a new dataframe
df = pd.DataFrame(data)
# we download it as a csv

# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

name_csv = f'../dashboard/dashboard_data/{brand_name}/page_views_info_{today}.csv'

df.to_csv(name_csv, index=False)