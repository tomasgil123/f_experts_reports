import os
import hmac
import streamlit as st
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

from dashboard.create_client_dashboard import create_dashboard
from dashboard.create_monthly_report import create_monthly_report
from utils import save_user_log


latico_leathers = "la44tico!"
tenzo_tea = "tenz44o!"
admin = "admin44!"
free_planet = "free44planet!"
the_perfect_jeans = "the77perfect!"
couleur_nature = "couleur22nature!"
caravan = "ca11ravan!"
bon_artis = "bon99artis!"
shinesty = "shi55nesty!"
lothantique = "22lothantique!"
boredwalk = "bo33redwalk!"
born_to_rally = "bo22rn_to_rally!"
true_classic = "true00classic!"
glimmer_wish = "glim22mer_wish!"
trek_light = "trek44light!"
little_hometown = "little44hometown!"
be_huppy = "be11huppy!"
grab2art = "grab22art!"
cheese_brothers = "cheese11bros!"
teleties = "tele99ties!"
medify = "medi00fy!"
tushy = "tushy88!"
future_kind = "future44kind!"
jack_archer = "jack22archer!"

inactive_clients = ['tenzo_tea', 'free_planet', 'the_perfect_jeans', 'couleur_nature', 'caravan', 'bon_artis', 'lothantique', 'boredwalk', 'born_to_rally', 'glimmer_wish', 'little_hometown', "trek_light", "true_classic", "shinesty", "tushy", "jack_archer", "grab2art", "future_kind", "cheese_brothers"]

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
    st.title("Login to Brand Caffeine analytics dashboard")
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
    

    # we filter clients that are inactive
    client_options = [client for client in client_options if client not in inactive_clients]
    sorted_client_options = sorted(client_options)

    default_client_option = sorted_client_options[0]

    client_option_selected = st.sidebar.radio("Select a client",  options=sorted_client_options, index=sorted_client_options.index(default_client_option), key=1)

    files = get_all_files_in_directory(f"./dashboard/dashboard_data/{client_option_selected}")

    report_options = ['SEO']
    #report_options = []

    if any("marketing_campaign_info" in file for file in files):
        report_options.append("Email marketing analytics")
    
    if any("page_views_info" in file for file in files):
        report_options.append("Product analytics")

    #if any("orders_from_api" in file for file in files):
    report_options.append("Order analytics")

    if any("competitors_data/product" in file for file in files) and any("competitors_data/reviews" in file for file in files):
        report_options.append("Competitors analytics")
    
    if any("competitors_data/custom_product" in file for file in files):
        report_options.append("Custom Competitors analytics")

    if any("brand_reviews" in file for file in files):
        report_options.append("Reviews")

    default_report_option = report_options[0]

    # we check starting_date of the brand
    starting_date = df_brands_reports[df_brands_reports["brand"] == client_option_selected]["starting_date"].values[0]

    display_monthly_reports = False

    # if current date is at least 30 days greater than starting date, we show the "Monthly Reports" expander
    if pd.to_datetime(starting_date) < pd.to_datetime("today") - pd.Timedelta(days=30):
        display_monthly_reports = st.sidebar.toggle("Display Monthly Reports", False)
        if display_monthly_reports:
            monthly_report_options = list_months(starting_date)
            monthly_report_option_selected = st.sidebar.radio("Select month", options=monthly_report_options, index=len(monthly_report_options)-1, key=3)
        
    report_option_selected = st.sidebar.radio("Select a report", options=report_options, index=report_options.index(default_report_option), key = 2)

    if display_monthly_reports:
        create_monthly_report(selected_client=client_option_selected, selected_month_string=monthly_report_option_selected, is_admin=True)
    else:
        create_dashboard(selected_client=client_option_selected, selected_report=report_option_selected, is_admin=True)
    
else:

    save_user_log(st.session_state["user_name"])

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

    if st.session_state["user_name"] == 'teleties':
         report_options.append("Order analytics")

    if any("competitors_data/product" in file for file in files) and any("competitors_data/reviews" in file for file in files):
        report_options.append("Competitors analytics")

    if any("competitors_data/custom_product" in file for file in files):
        report_options.append("Custom Competitors analytics")

    default_report_option = report_options[0]
    if st.session_state['user_name'] == 'latico_leathers':
        st.sidebar.title("----- -----")
    else:
        st.sidebar.title(convert_string(st.session_state['user_name']))

    # we check starting_date of the brand
    starting_date = df_brands_reports[df_brands_reports["brand"] == st.session_state["user_name"]]["starting_date"].values[0]
    
    display_monthly_reports = False

    # if current date is at least 30 days greater than starting date, we show the "Monthly Reports" expander
    if pd.to_datetime(starting_date) < pd.to_datetime("today") - pd.Timedelta(days=30):
        display_monthly_reports = st.sidebar.toggle("Display Monthly Reports", False)
        if display_monthly_reports:
            monthly_report_options = list_months(starting_date)
            monthly_report_option_selected = st.sidebar.radio("Select month", options=monthly_report_options, index=len(monthly_report_options)-1, key=3)
        
    report_option_selected = st.sidebar.radio("Select a report", options=report_options, index=report_options.index(default_report_option), key = 2)

    if display_monthly_reports:
        create_monthly_report(selected_client=st.session_state["user_name"], selected_month_string=monthly_report_option_selected, is_admin=False)
    else:
        create_dashboard(selected_client=st.session_state["user_name"], selected_report=report_option_selected, is_admin=False)