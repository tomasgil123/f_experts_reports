import glob
import pandas as pd
from get_orders_brand_info import (get_orders_info)
from cookie import (cookie_token)

from utils import (get_orders_teleties, get_orders_items_teleties)

# brand_token = "b_cad0ccd3"
# brand_name = "couleur_nature"

# brand_token = "b_bdz7u5jj94"
# brand_name = "caravan"

# brand_token = "b_cmvrf26fxf"
# brand_name = "bon_artis"

# brand_token = "b_67e3bc3f"
# brand_name = "lothantique"

# brand_token = "b_vsxe65ezpv"
# brand_name = "glimmer_wish"

# brand_token = "b_arceup81f2"
# brand_name = "latico_leathers"

# brand_token = "b_4vbanx86sk"
# brand_name = "little_hometown"

# brand_token = "b_9j68t72ipo"
# brand_name = "true_classic"

# brand_token = "b_vllag6pj"
# brand_name = "trek_light"

# ====================

# brand_token = "b_f65wemh3b7"
# brand_name = "be_huppy"

# brand_token = "b_9884o1r7ea"
# brand_name = "shinesty"

brand_token = "b_12tpkawx"
brand_name = "teleties"

# brand_token = "b_fg3z6jazys"
# brand_name = "medify"

# brand_token = "b_1c6eqlam"
# brand_name = "dolan_geiman"

# brand_token = "b_aqaeteuq89"
# brand_name = "viori"

# brand_token = "b_abnh48rfz1"
# brand_name = "levtex_home"




# brand_token = "b_2j1b52vu"
# brand_name = "grab2art"

# brand_token = "b_2dvofcgxz7"
# brand_name = "cheese_brothers"

# brand_token = "b_4v6l6ww3o7"
# brand_name = "tushy"

# brand_token = "b_ewdnueckng"
# brand_name = "future_kind"

# brand_token = "b_ekmpt42px"
# brand_name = "jack_archer"

 # df_current_marketing_campaign_info is an empty dataframe
df_current_orders = pd.DataFrame()
df_current_items_order = pd.DataFrame()

if brand_name == "teleties-":
    df_current_orders = get_orders_teleties()
    df_current_items_order = get_orders_items_teleties()

    # identify campaign with the most recent brand_contacted_at_value date
    time_most_recent_campaign = df_current_orders['brand_contacted_at_values'].max()

    # we substract a month to the time_most_recent_campaign
    # we do this because some orders attributes could have been updated. We assume older orders don't get updated anymore
    time_most_recent_campaign = time_most_recent_campaign - 2630304000
    
else:
    # we check if there is data already downloaded
    orders_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/orders_from_api_*.csv")
    items_order_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/items_order_from_api_*.csv")

    # create variable time_most_recent_campaign using default Unix epoch timestamp
    time_most_recent_campaign = 0

    if len(orders_file) > 0:
        df_current_orders = pd.read_csv(orders_file[0])

        if len(items_order_file) > 0:
            df_current_items_order = pd.read_csv(items_order_file[0])

        # identify campaign with the most recent brand_contacted_at_value date
        time_most_recent_campaign = df_current_orders['brand_contacted_at_values'].max()

        # we substract a month to the time_most_recent_campaign
        # we do this because some orders attributes could have been updated. We assume older orders don't get updated anymore
        time_most_recent_campaign = time_most_recent_campaign - 2630304000


orders, items_order = get_orders_info(brand_token, cookie=cookie_token, time_most_recent_campaign=time_most_recent_campaign)

# we convert both object to pandas dataframes
df_orders = pd.DataFrame(orders)
df_items_order = pd.DataFrame(items_order)

df_orders = pd.concat([df_orders, df_current_orders], ignore_index=True)
df_items_order = pd.concat([df_items_order, df_current_items_order], ignore_index=True)

# we drop duplicates
df_orders = df_orders.drop_duplicates(subset='tokens', keep='first')
df_items_order = df_items_order.drop_duplicates(subset='token', keep='first')

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