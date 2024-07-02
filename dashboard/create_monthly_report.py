import streamlit as st
import glob
import pandas as pd

from dashboard.monthly_analytics import (sales_performance_metrics, get_marketing_campaign_sales, customer_acquisition_metrics)
from dashboard.utils import (save_user_log_report, get_orders_teleties)

def create_monthly_report(selected_client, selected_month_string, is_admin):

    # if is admin is false, we save log
    if not is_admin:
        save_user_log_report(selected_client, "Monthly Report")

    st.markdown(f"""
                # Monthly Report: {selected_month_string}
                ### Total sales, average order value and orders
                Only orders with status 'Delivered' or 'Shipped' and type 'New Order' were considered.
                """)
    
    selected_month_date = pd.to_datetime(selected_month_string)
    selected_month = selected_month_date.month
    selected_year = selected_month_date.year
    
    if selected_client == "teleties":
        df_orders = get_orders_teleties()
    else:

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/orders_from_api_*.csv")

        df_orders = pd.read_csv(product_file[0])

    df_orders['payout_total_values'] = df_orders['payout_total_values']/100

    # Convert 'brand_contacted_at_values' to datetime
    df_orders['brand_contacted_at_values'] = pd.to_datetime(df_orders['brand_contacted_at_values'], unit='ms')

    # Filter orders where creation_reasons is equal to NEW_ORDER
    df_orders = df_orders[(df_orders['creation_reasons'] == 'NEW_ORDER') & ((df_orders['states'] == 'SHIPPED') | (df_orders['states'] == 'DELIVERED'))]

    sales_performance_metrics(df_orders, selected_month, selected_year, selected_month_string)

    st.markdown("""
                    # 
                    ### Sales generated through email marketing initiatives
                    """)
        

    product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/marketing_campaign_info_*.csv")

    df_marketing = pd.read_csv(product_file[0])
    df_marketing_completed_campaigns = df_marketing[df_marketing['states'] == 'COMPLETED']

    # Convert 'start_sending_at' to datetime
    df_marketing_completed_campaigns['start_sending_at'] = pd.to_datetime(df_marketing_completed_campaigns['start_sending_at'], unit='ms')

    get_marketing_campaign_sales(df_marketing_completed_campaigns, selected_month, selected_year)

    st.markdown("""
                # 
                ### Customer acquisition
                """)

    customer_acquisition_metrics(df_orders, selected_month, selected_year, selected_month_string)
    