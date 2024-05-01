from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import streamlit as st

# Define the scope of the application
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def save_user_log(client_name):
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
    range_name = 'Logs'  # Example sheet name

    # How the input data should be interpreted.
    value_input_option = 'USER_ENTERED' 

    # How the input data should be inserted.
    insert_data_option = 'INSERT_ROWS'

    current_datetime = datetime.now().strftime('%m/%d/%Y %H:%M:%S') 

    value_range_body = {
        "values": [
            [client_name, current_datetime]  # Your new row data here
        ]
    }

    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_name,
                                                     valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()

    print(response)