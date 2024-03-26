
import pandas as pd
from get_customers_crm import get_customer_crm
from cookie import (cookie_token)

# brand_token = "b_9884o1r7ea"

# data = get_customer_crm(brand_token, cookie=cookie_token, page_number=230)

# # download to csv


# df = pd.DataFrame(data)
# df.to_csv("customer_data.csv", index=False)

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

df = pd.read_csv("merged_customer_data.csv")

# keep rows with unique email addresses, but keep rows where email address is None
df = df.drop_duplicates(subset=["email_address"])

# Convert Unix timestamps to datetime format
df['last_contacted'] = pd.to_datetime(df['last_contacted'], unit='ms', errors='coerce')
df['signed_up_at'] = pd.to_datetime(df['signed_up_at'], unit='ms', errors='coerce')

# Format the datetime columns to mm/dd/yyyy
df['last_contacted'] = df['last_contacted'].dt.strftime('%m/%d/%Y')
df['signed_up_at'] = df['signed_up_at'].dt.strftime('%m/%d/%Y')

# download csv 
df.to_csv("unique_customer_data.csv", index=False)