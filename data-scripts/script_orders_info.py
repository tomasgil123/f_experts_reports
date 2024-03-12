import pandas as pd
from get_orders_brand_info import (get_orders_info)
from cookie import (cookie_token)

brand_token = "b_9j68t72ipo"
brand_name = "true_classic"

orders, items_order = get_orders_info(brand_token, cookie=cookie_token)

# we convert both object to pandas dataframes
df_orders = pd.DataFrame(orders)
df_items_order = pd.DataFrame(items_order)

# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

# As the time being, we need first to create the folder where we will save the csv files
# they are not automatically generated
name_orders_csv = f'../dashboard/dashboard_data/{brand_name}/orders_from_api_{today}.csv'
name_items_order_csv = f'../dashboard/dashboard_data/{brand_name}/items_order_from_api_{today}.csv'

df_orders.to_csv(name_orders_csv, index=False)
df_items_order.to_csv(name_items_order_csv, index=False)