
from get_customers_crm import get_customers
from cookie import (cookie_token)

# brand_token = "b_vllag6pj"
# brand_token = "b_9884o1r7ea"
# brand_name = "shinesty"

# brand_token = "b_cad0ccd3"
# brand_name = "Couleur_nature"

# brand_token = "b_bdz7u5jj94"
# brand_name = "caravan"

# brand_token = "b_cmvrf26fxf"
# brand_name = "bon_artis"

# brand_token = "b_9j68t72ipo"
# brand_name = "true_classic"

# brand_token = "b_vsxe65ezpv"
# brand_name = "glimmer_wish"

brand_token = "b_vllag6pj"
brand_name = "trek_light"

get_customers(brand_token, cookie=cookie_token, page_number=1, brand_name=brand_name)

# import os

# # Current directory
# current_directory = os.getcwd()

# # List all files in the current directory
# files_in_directory = os.listdir(current_directory)

# # Pattern for file names
# file_pattern = 'customer_data_page_'

# # List to store data frames
# dfs = []

# # Loop through files in directory
# for filename in files_in_directory:
#     if filename.startswith(file_pattern) and filename.endswith('.csv'):
#         # Read CSV file
#         df = pd.read_csv(filename)
#         print(df)
#         # Append to list
#         dfs.append(df)

# # Concatenate data frames
# merged_df = pd.concat(dfs, ignore_index=True)

# # Write merged dataframe to a new CSV file
# merged_df.to_csv('./merged_customer_data.csv', index=False)

# df = pd.read_csv("merged_customer_data.csv")

# # keep rows with unique email addresses, but keep rows where email address is None
# df = df.drop_duplicates(subset=["email_address"])

# # Convert Unix timestamps to datetime format
# df['last_contacted'] = pd.to_datetime(df['last_contacted'], unit='ms', errors='coerce')
# df['signed_up_at'] = pd.to_datetime(df['signed_up_at'], unit='ms', errors='coerce')

# # Format the datetime columns to mm/dd/yyyy
# df['last_contacted'] = df['last_contacted'].dt.strftime('%m/%d/%Y')
# df['signed_up_at'] = df['signed_up_at'].dt.strftime('%m/%d/%Y')

# # download csv 
# df.to_csv("unique_customer_data.csv", index=False)