import pandas as pd
import glob

from get_reviews_utils import (get_reviews)
from cookie import (cookie_token)

# brand_token = "b_1c6eqlam"
# brand_name = "dolan_geiman"

brand_token = "b_aqaeteuq89"
brand_name = "viori"

# brand_token = "b_abnh48rfz1"
# brand_name = "levtex_home"

# brand_token = "b_12tpkawx"
# brand_name = "teleties"

# # we check if there is data already downloaded
product_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/brand_reviews_*.csv")

# create variable time_most_recent_campaign using default Unix epoch timestamp
time_most_recent_review = 0

# df_current_marketing_campaign_info is an empty dataframe
df_current_review = pd.DataFrame()

if len(product_file) > 0:
    df_current_review = pd.read_csv(product_file[0])

    # identify campaign with the most recent start_sending_at date
    time_most_recent_review = df_current_review['start_sending_at'].max()

    # we substract a month to the time_most_recent_campaign
    # we do this because some campaign attributes could have been updated. We assume older campaigns don't get updated anymore
    time_most_recent_review = time_most_recent_review - 2630304000
   
reviews_info = get_reviews(brand_token, cookie=cookie_token, time_most_recent_review=time_most_recent_review)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(reviews_info)

# we append to df_current_marketing_campaign_info the new data
df = pd.concat([df, df_current_review], ignore_index=True)

# we drop duplicates
df = df.drop_duplicates(subset='token', keep='first')

# get today date
today = pd.to_datetime('today').date()
# convert it to a string with format yyyy/mm/dd
today = today.strftime('%Y-%m-%d')

name_csv = f'../dashboard/dashboard_data/{brand_name}/brand_reviews_{today}.csv'

df.to_csv(name_csv, index=False)