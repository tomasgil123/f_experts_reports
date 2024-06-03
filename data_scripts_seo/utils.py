from datetime import datetime, timedelta
import os
from datetime import datetime, timedelta
import pandas as pd
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import streamlit as st
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

def filter_unique_objects(objects):
    seen = set()
    unique_objects = []

    for obj in objects:
        identifier = (obj['brand_token'], obj['title'])
        if identifier not in seen:
            seen.add(identifier)
            unique_objects.append(obj)

    return unique_objects


def generate_date_array(start_date):
    # Convert the start_date string to a datetime object
    start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')
    # Get yesterday's date
    end_date_obj = datetime.today() - timedelta(days=1)

    # Generate a list of dates from start_date to today
    date_array = []
    current_date = start_date_obj
    while current_date <= end_date_obj:
        date_array.append(current_date.strftime('%Y-%m-%d'))
        current_date += timedelta(days=1)

    return date_array

# Define the scope of the application
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# Access the environment variables
openai_api_key = os.getenv('openai_api_key')
project_id = os.getenv('project_id')
private_key_id = os.getenv('private_key_id')
private_key = os.getenv('private_key')
client_email = os.getenv('client_email')
client_id = os.getenv('client_id')
client_x509_cert_url = os.getenv('client_x509_cert_url')

def get_data_from_google_spreadsheet(spreadsheet_id, range_name):

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

    creds = Credentials.from_service_account_info(creds_dict, scopes=SCOPES)
    service = build('sheets', 'v4', credentials=creds)

    # Use the Sheets API to get the data
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    # Check if data was retrieved successfully
    if not values:
        return pd.DataFrame()
    else:
        # Create a DataFrame
        df = pd.DataFrame(values[1:], columns=values[0])
        return df