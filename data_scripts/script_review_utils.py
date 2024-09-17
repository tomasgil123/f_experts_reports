import pandas as pd
import glob
from datetime import datetime

from get_reviews_utils import (get_reviews)
from cookie import (cookie_token)

# brand_token = "b_12tpkawx"
# brand_name = "teleties"

# brand_token = "b_1c6eqlam"
# brand_name = "dolan_geiman"

#brand_token = "b_aqaeteuq89"
#brand_name = "viori"

#brand_token = "b_abnh48rfz1"
#brand_name = "levtex_home"

brand_token = "b_4v6l6ww3o7"
brand_name = "tushy"

# brand_token = "b_fg3z6jazys"
# brand_name = "medify"


# Check if there is data already downloaded
product_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/brand_reviews_*.csv")

# Initialize variables
time_most_recent_review = 0
df_current_review = pd.DataFrame()

if len(product_file) > 0:
    df_current_review = pd.read_csv(product_file[0])
    
    if not df_current_review.empty:
        # Identify the most recent review date
        time_most_recent_review = df_current_review['created_at'].max()
        
        # Convert milliseconds to seconds (Unix timestamp)
        time_most_recent_review = int(time_most_recent_review / 1000)
        
        # Add 1 second to ensure we don't duplicate the last review
        time_most_recent_review += 1

# Get new reviews
reviews_info = get_reviews(brand_token, cookie=cookie_token, time_most_recent_review=time_most_recent_review)

# Convert new reviews to a dataframe
df_new_reviews = pd.DataFrame(reviews_info)

# Combine new and existing reviews
df = pd.concat([df_new_reviews, df_current_review], ignore_index=True)

# Drop duplicates
df = df.drop_duplicates(subset='token', keep='first')

# Get today's date
today = datetime.now().strftime('%Y-%m-%d')

# Save to CSV
name_csv = f'../dashboard/dashboard_data/{brand_name}/brand_reviews_{today}.csv'
df.to_csv(name_csv, index=False)