import pandas as pd
from get_orders_brand_info import (get_orders_info)
from cookie import (cookie_token)

# brand_token = "b_cad0ccd3"
# brand_name = "couleur_nature"

brand_token = "b_bdz7u5jj94"
brand_name = "caravan"

# brand_token = "b_cmvrf26fxf"
# brand_name = "bon_artis"

# brand_token = "b_67e3bc3f"
# brand_name = "lothantique"

# brand_token = "b_9884o1r7ea"
# brand_name = "shinesty"

# brand_token = "b_vtmq6kd56j"
# brand_name = "born_to_rally"

# brand_token = "b_vsxe65ezpv"
# brand_name = "glimmer_wish"

# brand_token = "b_vllag6pj"
# brand_name = "trek_light"

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