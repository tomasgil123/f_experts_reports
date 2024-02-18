import pandas as pd
from get_product_views_info import (get_page_views_for_all_months_since_date)
from cookie import (cookie_token)

data = get_page_views_for_all_months_since_date(cookie=cookie_token, starting_date="2023-01-01")

# we create a new dataframe
df = pd.DataFrame(data)
# we download it as a csv
df.to_csv('page_views_info.csv', index=False)