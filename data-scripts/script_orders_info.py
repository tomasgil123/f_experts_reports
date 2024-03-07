import pandas as pd
from get_orders_brand_info import (get_orders_info)
from cookie import (cookie_token)

brand_token = "b_vtmq6kd56j" 

orders_info = get_orders_info(brand_token, cookie=cookie_token)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(orders_info)
# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

name_csv = f'orders_from_api_{today}.csv'

df.to_csv(name_csv, index=False)