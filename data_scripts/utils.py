import re
from datetime import datetime, timedelta
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import streamlit as st
import os
from google.cloud import storage
from io import StringIO
from google.api_core.exceptions import NotFound
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

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

def download_csv_from_cloud_storage(bucket_name, source_blob_name):

    project_id = os.getenv('project_id')
    private_key_id = os.getenv('private_key_id')
    private_key = os.getenv('private_key')
    client_email = os.getenv('client_email')
    client_id = os.getenv('client_id')
    client_x509_cert_url = os.getenv('client_x509_cert_url')

    creds_dict = {
        "type": "service_account",
        "project_id": project_id,
        "private_key_id": private_key_id,
        "private_key": private_key.replace('\\n', '\n'),
        "client_email": client_email,
        "client_id": client_id,
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": client_x509_cert_url
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