import pandas as pd
from get_marketing_campaigns_info import (get_marketing_campaigns_info)
from cookie import (cookie_token)

brand_token = "b_bdz7u5jj94"

marketing_campaign_info = get_marketing_campaigns_info(brand_token, cookie=cookie_token)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(marketing_campaign_info)

# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

name_csv = f'marketing_campaign_info_{today}.csv'

df.to_csv(name_csv, index=False)