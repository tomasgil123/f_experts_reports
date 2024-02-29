import pandas as pd
from get_orders_brand_info import (get_orders_info)
from cookie import (cookie_token)

brand_token = "b_cad0ccd3"

orders_info = get_orders_info(brand_token, cookie=cookie_token)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(orders_info)
df.to_csv('orders_from_api.csv', index=False)