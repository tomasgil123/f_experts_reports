import re
from datetime import datetime, timedelta
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import streamlit as st

from google.cloud import storage
from io import StringIO
from google.api_core.exceptions import NotFound

def read_md_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()
    
def get_text_between_comments(text, start_comment, end_comment):
    start_index = text.find(start_comment)
    if start_index == -1:
        return None  # Start comment not found
    end_index = text.find(end_comment, start_index + len(start_comment))
    if end_index == -1:
        return None  # End comment not found
    return text[start_index + len(start_comment):end_index].strip()

def extract_date_from_filename(file_name):
    """
    Extracts the date from a file name in the format 'orders_from_api_YYYY-MM-DD'.
    
    Args:
    file_name (str): The name of the file.
    
    Returns:
    datetime object: The extracted date.
    None: If date is not found in the file name.
    """
    # Define a regular expression pattern to match the date
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    
    # Use regex to find the date pattern in the file name
    match = re.search(date_pattern, file_name)

    if match:
        # Extract the matched date string
        date_str = match.group(0)

        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        
        return date_obj
    else:
        return None
    

# Define the scope of the application
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def save_user_log_report(client_name, selected_report):
    creds_dict = {
        "type": "service_account",
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }

    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # The ID of the spreadsheet to update.
    spreadsheet_id = '1rdGzjnDo8IYhQZ3sUB2N91Zx2M2FfwpkWOBn0FwWcHk'  # Please set the Spreadsheet ID.
    range_name = 'App_logs'  # Example sheet name

    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED' 

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    current_datetime = datetime.now().strftime('%m/%d/%Y %H:%M:%S') 

    value_range_body = {
        "values": [
            [client_name, current_datetime, selected_report]  # Your new row data here
        ]
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name,
                                                     valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()

    print(response)

def get_data_from_google_spreadsheet(spreadsheet_id, range_name):

    creds_dict = {
        "type": "service_account",
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }

    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Use the Sheets API to get the data
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    print("values", len(values[0]))
    print(values[0])
    print("values 1", len(values[1]))

    # Check if data was retrieved successfully
    if not values:
        return pd.DataFrame()
    else:
        # Create a DataFrame
        df = pd.DataFrame(values[1:], columns=values[0])
        return df
    

def snake_to_title(snake_str):
    # Split the string by underscores
    components = snake_str.split('_')
    # Capitalize the first letter of each component and join them with a space
    title_str = ' '.join(x.capitalize() for x in components)
    return title_str

def get_orders_teleties():

    # Get the data from the Google Cloud Storage bucket
    bucket_name = "faire_reports_old"
    source_blob_name = "orders_from_api_2024-06-20"

    df_orders = download_csv_from_cloud_storage(bucket_name, source_blob_name)

    # df_marketing_info is None we return an empty dataframe
    if df_orders is None:
        return pd.DataFrame()
    else:
        return df_orders
    
def get_orders_items_teleties():

    # Get the data from the Google Cloud Storage bucket
    bucket_name = "faire_reports_old"
    source_blob_name = "items_order_from_api_2024-06-20"

    df_orders = download_csv_from_cloud_storage(bucket_name, source_blob_name)

    print("=============================")
    print(len(df_orders))

    # df_marketing_info is None we return an empty dataframe
    if df_orders is None:
        return pd.DataFrame()
    else:
        return df_orders

@st.cache_data(ttl=36000)  # Cache data for 1 hour (3600 seconds)
def download_csv_from_cloud_storage(bucket_name, source_blob_name):

    creds_dict = {
        "type": "service_account",
        "project_id": st.secrets["project_id"],
        "private_key_id": st.secrets["private_key_id"],
        "private_key": st.secrets["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["client_email"],
        "client_id": st.secrets["client_id"],
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": st.secrets["client_x509_cert_url"]
    }

    try:
        # Create credentials object from the dictionary
        credentials = Credentials.from_service_account_info(creds_dict)

        # Create a client to interact with the Google Cloud Storage API
        storage_client = storage.Client(credentials=credentials, project=creds_dict["project_id"])

        # Get the bucket where the file is stored
        bucket = storage_client.get_bucket(bucket_name)

        blobs = bucket.list_blobs(prefix=source_blob_name)

        csv_data = None
        blob_name = None

        # this way we are only keeping the first blob
        for blob in blobs:
            # Download the file content as a string
            csv_data = blob.download_as_text()
            blob_name = blob.name
            break
        
        if csv_data is not None:
            # Use pandas to read the CSV data
            df = pd.read_csv(StringIO(csv_data))
        else:
            df = pd.DataFrame()

        return df

    except NotFound:
        print(f"The file '{source_blob_name}' does not exist in the bucket '{bucket_name}'.")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None