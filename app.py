import os
import hmac
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

from dashboard.create_client_dashboard import create_dashboard
from dashboard.create_monthly_report import create_monthly_report

openai_api_key = st.secrets["openai_api_key"]

if openai_api_key != "":
    os.environ['OPENAI_API_KEY'] = openai_api_key

def convert_string(string):
    # Replace "_" with space
    string = string.replace("_", " ")
    
    # Capitalize each word
    string = string.title()
    
    return string

def list_months(start_date):
    # Convert the start date string to a datetime object
    start_date = datetime.strptime(start_date, '%m-%d-%Y')
    
    # Get the current date
    current_date = datetime.now()
    
    # Initialize an empty list to store the month names
    months_list = []
    
    # Iterate over months from the start date until the previous month of the current month
    while start_date < datetime(current_date.year, current_date.month, 1):
        months_list.append(start_date.strftime('%B %Y'))  # Append month name to the list
        start_date += relativedelta(months=1)  # Increment by one month
    
    return months_list

with open("custom.css") as f:
    custom_css = f.read()

# Use st.markdown to inject the CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

def get_all_files_in_directory(directory):
    files = []
    # os.walk returns a generator, that creates a tuple of values
    # (current_path, directories in current_path, files in current_path).
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            files.append(os.path.join(dirpath, file))
    return files

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["is_admin"] = st.session_state["username"] == "admin"
            st.session_state["user_name"] = st.session_state["username"]
            st.session_state["password_correct"] = True
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    st.title("Login to FaireExperts analytics dashboard")
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False


if not check_password():
    st.stop()

# Main Streamlit app starts here
    
st.markdown(
    """
    <style>
        [data-testid=stSidebar] [data-testid=stImage]{
            text-align: center;
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 100%;
            margin-top: -75px;
        }
    </style>
    """, unsafe_allow_html=True
)
st.sidebar.image('brand_caffeine_logo.png', caption='', width=150)

if st.session_state.get("is_admin", False):

    df_brands_reports = pd.read_csv("./brands_monthly_reports.csv")

    client_options = [key for key in st.secrets["passwords"] if key != "admin"]
    sorted_client_options = sorted(client_options)

    default_client_option = sorted_client_options[0]

    client_option_selected = st.sidebar.radio("Select a client",  options=sorted_client_options, index=sorted_client_options.index(default_client_option), key=1)

    files = get_all_files_in_directory(f"./dashboard/dashboard_data/{client_option_selected}")

    report_options = []

    if any("marketing_campaign_info" in file for file in files):
        report_options.append("Email marketing analytics")
    
    if any("page_views_info" in file for file in files):
        report_options.append("Product analytics")

    if any("orders_from_api" in file for file in files):
        report_options.append("Order analytics")

    if any("competitors_data/product" in file for file in files) and any("competitors_data/reviews" in file for file in files):
        report_options.append("Competitors analytics")
    
    if any("competitors_data/custom_product" in file for file in files):
        report_options.append("Custom Competitors analytics")

    default_report_option = report_options[0]

    # we check starting_date of the brand
    starting_date = df_brands_reports[df_brands_reports["brand"] == client_option_selected]["starting_date"].values[0]

    # if current date is at least 30 days greater than starting date, we show the "Monthly Reports" expander
    if pd.to_datetime(starting_date) < pd.to_datetime("today") - pd.Timedelta(days=30):
        display_monthly_reports = st.sidebar.toggle("Display Monthly Reports", False)
        if display_monthly_reports:
            monthly_report_options = list_months(starting_date)
            monthly_report_option_selected = st.sidebar.radio("Select month", options=monthly_report_options, index=len(monthly_report_options)-1, key=3)
        
    report_option_selected = st.sidebar.radio("Select a report", options=report_options, index=report_options.index(default_report_option), key = 2)

    if display_monthly_reports:
        create_monthly_report(selected_client=client_option_selected, selected_month_string=monthly_report_option_selected)
    else:
        create_dashboard(selected_client=client_option_selected, selected_report=report_option_selected)
    
else:
    df_brands_reports = pd.read_csv("./brands_monthly_reports.csv")
    # these report options depend on the files the client has
    # get all files in folder ./dahsboard/dashboard_data/{selected_client}

    files = get_all_files_in_directory(f"./dashboard/dashboard_data/{st.session_state['user_name']}")

    report_options = []

    if any("marketing_campaign_info" in file for file in files):
        report_options.append("Email marketing analytics")
    
    if any("page_views_info" in file for file in files):
        report_options.append("Product analytics")

    if any("orders_from_api" in file for file in files):
        report_options.append("Order analytics")

    if any("competitors_data/product" in file for file in files) and any("competitors_data/reviews" in file for file in files):
        report_options.append("Competitors analytics")

    if any("competitors_data/custom_product" in file for file in files):
        report_options.append("Custom Competitors analytics")

    default_report_option = report_options[0]

    st.sidebar.title(convert_string(st.session_state['user_name']))

    # report_option_selected = st.sidebar.radio("Select a report", options=report_options, index=report_options.index(default_report_option), key = 2)

    # create_dashboard(selected_client=st.session_state["user_name"], selected_report=report_option_selected)
    
    # we check starting_date of the brand
    starting_date = df_brands_reports[df_brands_reports["brand"] == st.session_state["user_name"]]["starting_date"].values[0]

    # if current date is at least 30 days greater than starting date, we show the "Monthly Reports" expander
    if pd.to_datetime(starting_date) < pd.to_datetime("today") - pd.Timedelta(days=30):
        display_monthly_reports = st.sidebar.toggle("Display Monthly Reports", False)
        if display_monthly_reports:
            monthly_report_options = list_months(starting_date)
            monthly_report_option_selected = st.sidebar.radio("Select month", options=monthly_report_options, index=len(monthly_report_options)-1, key=3)
        
    report_option_selected = st.sidebar.radio("Select a report", options=report_options, index=report_options.index(default_report_option), key = 2)

    if display_monthly_reports:
        create_monthly_report(selected_client=st.session_state["user_name"], selected_month_string=monthly_report_option_selected)
    else:
        create_dashboard(selected_client=st.session_state["user_name"], selected_report=report_option_selected)