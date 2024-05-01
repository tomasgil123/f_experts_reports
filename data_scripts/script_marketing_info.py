import pandas as pd
import glob

from get_marketing_campaigns_info import (get_marketing_campaigns_info)
from cookie import (cookie_token)

# brand_token = "b_9j68t72ipo"
# brand_name = "true_classic"

# brand_token = "b_cad0ccd3"
# brand_name = "couleur_nature"

# brand_token = "b_bdz7u5jj94"
# brand_name = "caravan"

# brand_token = "b_cmvrf26fxf"
# brand_name = "bon_artis"

brand_token = "b_67e3bc3f"
brand_name = "lothantique"

# brand_token = "b_9884o1r7ea"
# brand_name = "shinesty"

# brand_token = "b_vtmq6kd56j"
# brand_name = "born_to_rally"

# brand_token = "b_vsxe65ezpv"
# brand_name = "glimmer_wish"

# brand_token = "b_vllag6pj"
# brand_name = "trek_light"

# brand_token = "b_arceup81f2"
# brand_name = "latico_leathers"

# # we check if there is data already downloaded
product_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/marketing_campaign_info_*.csv")

# create variable time_most_recent_campaign using default Unix epoch timestamp
time_most_recent_campaign = 0

# df_current_marketing_campaign_info is an empty dataframe
df_current_marketing_campaign_info = pd.DataFrame()

if len(product_file) > 0:
    df_current_marketing_campaign_info = pd.read_csv(product_file[0])

    # identify campaign with the most recent start_sending_at date
    time_most_recent_campaign = df_current_marketing_campaign_info['start_sending_at'].max()

    # we substract a month to the time_most_recent_campaign
    # we do this because some campaign attributes could have been updated. We assume older campaigns don't get updated anymore
    time_most_recent_campaign = time_most_recent_campaign - 2630304000
   
marketing_campaign_info = get_marketing_campaigns_info(brand_token, cookie=cookie_token, time_most_recent_campaign=time_most_recent_campaign)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(marketing_campaign_info)

# we append to df_current_marketing_campaign_info the new data
df = pd.concat([df, df_current_marketing_campaign_info], ignore_index=True)

# we drop duplicates
df = df.drop_duplicates(subset='tokens', keep='first')

# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

name_csv = f'../dashboard/dashboard_data/{brand_name}/marketing_campaign_info_{today}.csv'

df.to_csv(name_csv, index=False)