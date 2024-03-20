import streamlit as st
import pandas as pd
import glob
import os
from datetime import datetime

def list_files_in_directory(directory_path):
    with os.scandir(directory_path) as entries:
        for entry in entries:
            print(entry.name)

def get_creation_time(file_path):
    return os.path.getctime(file_path)

def get_last_update_time(file_path):
    last_update_data = get_creation_time(file_path)
        # Convert timestamp to datetime object
    dt_object = datetime.fromtimestamp(last_update_data)

    # Format datetime object as MM/dd/yyyy
    formatted_date = dt_object.strftime("%m/%d/%Y")

    st.markdown(f"Data was last updated at: {formatted_date}")

from dashboard.product_analytics_charts import (generate_pageviews_orders_ratio_chart, 
                    generate_page_views_chart_by_category_last_12_months,
                    generate_page_views_evolution_last_12_months_by_category,
                    generates_sales_chart_by_category_last_12_months,
                    generate_page_views_chart_by_product_last_12_months, 
                    generate_page_views_and_ratio_by_category_with_selector, 
                    generate_conversion_rate_chart_by_category,
                    generate_page_views_and_ratio_by_product_with_selector)

from dashboard.order_analytics_charts import (lifetime_performance_metrics, sales_per_quarter, 
                                    sales_previous_year_vs_sales_year_before_that_one,
                                    orders_previous_year_vs_orders_year_before_that_one, sales_by_source,
                                    new_merchants_by_source, sales_by_retailer, cumulative_distribution_of_retailers,
                                    type_of_store_top_10_retailers, sales_distribution, sales_quantiles, purchase_frequency, retailers_did_not_reorder)


from dashboard.email_marketing_analytics_charts import (get_email_marketing_kpis_last_30_days, 
                                              get_email_marketing_kpis_by_month, sales_by_month)

from dashboard.utils import (extract_date_from_filename, read_md_file, get_text_between_comments)

# Dashboard creation
from dashboard.create_competitors_dashboard import (create_competitors_dashboard, create_custom_competitors_dashboard)


def create_dashboard(selected_client, selected_report):

    markdown_text = read_md_file(f"./dashboard/dashboard_text/{selected_client}/texts.md")
    
    if selected_report == "Email marketing analytics":

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/marketing_campaign_info_*.csv")

        date_last_update = extract_date_from_filename(product_file[0])

        st.write(f"Data was last updated at: {date_last_update.date()}")

        data = pd.read_csv(product_file[0])

        st.markdown("""
                # Email Marketing Analytics
                ### Email performance review
                Last 30 days:
                """)

        get_email_marketing_kpis_last_30_days(data, date_last_update)

        get_email_marketing_kpis_by_month(data)

        sales_by_month(data, 'open_based_total_order_value', 'Total Sales Open emails (12 months)', date_last_update)
        sales_by_month(data, 'click_based_total_order_value', 'Total Sales Click emails (12 months)', date_last_update)

        product_file_orders = glob.glob(f"./dashboard/dashboard_data/{selected_client}/orders_from_api_*.csv")

        date_last_update_orders = extract_date_from_filename(product_file_orders[0])

        df_orders = pd.read_csv(product_file_orders[0])

        df_orders['payout_total_values'] = df_orders['payout_total_values']/100

        # Convert 'brand_contacted_at_values' to datetime
        df_orders['brand_contacted_at_values'] = pd.to_datetime(df_orders['brand_contacted_at_values'], unit='ms')

        # Filter orders where creation_reasons is equal to NEW_ORDER
        df_orders = df_orders[(df_orders['creation_reasons'] == 'NEW_ORDER') & ((df_orders['states'] == 'SHIPPED') | (df_orders['states'] == 'DELIVERED'))]

        st.markdown("""
                    #
                ### Campaign ideas
                #### Re-engagement campaigns
                """)
        
        reengagement_campaigns = get_text_between_comments(markdown_text, "<!-- Email marketing: Campaign ideas -->", "<!")
        if reengagement_campaigns is not None:
            st.markdown(reengagement_campaigns, unsafe_allow_html=True)
        
        cumulative_distribution_of_retailers(df_orders, day_data_was_obtained=date_last_update_orders)

        sales_by_retailer(df_orders, day_data_was_obtained=date_last_update_orders)

        sales_quantiles(df_orders, day_data_was_obtained=date_last_update_orders)

        purchase_frequency(df_orders)

        retailers_did_not_reorder(df_orders)

    elif selected_report == "Product analytics":

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/page_views_info_*.csv")

        date_last_update = extract_date_from_filename(product_file[0])

        st.write(f"Data was last updated at: {date_last_update.date()}")

        data = pd.read_csv(product_file[0])

        data['date'] = pd.to_datetime(data['date'])

        st.markdown(f"# Product Analytics")

        generate_page_views_chart_by_category_last_12_months(data, date_last_update)

        generate_page_views_evolution_last_12_months_by_category(data)

        page_views_by_category_analysis = get_text_between_comments(markdown_text, "<!-- Product: page views by category last 12 months -->", "<!")
        if page_views_by_category_analysis is not None:
            st.markdown(page_views_by_category_analysis, unsafe_allow_html=True)

        # generate_page_views_chart_by_product_last_12_months(data, date_last_update)
            
        # generates_sales_chart_by_category_last_12_months(data, date_last_update)

        generate_conversion_rate_chart_by_category(data, date_last_update)

        conversion_category_analysis = get_text_between_comments(markdown_text, "<!-- Product: conversion by category -->", "<!")
        if conversion_category_analysis is not None:
            st.markdown(conversion_category_analysis, unsafe_allow_html=True)

        generate_pageviews_orders_ratio_chart(data, date_last_update)

        conversion_product_analysis = get_text_between_comments(markdown_text, "<!-- Product: conversion by product -->", "<!")
        if conversion_product_analysis is not None:
            st.markdown(conversion_product_analysis, unsafe_allow_html=True)

        generate_page_views_and_ratio_by_category_with_selector(data)

        generate_page_views_and_ratio_by_product_with_selector(data)

    elif selected_report == "Order analytics":

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/orders_from_api_*.csv")

        date_last_update = extract_date_from_filename(product_file[0])

        st.write(f"Data was last updated at: {date_last_update.date()}")

        st.markdown("""
                    # Order Analytics
                    ### Total sales, average order value and orders
                    Only orders with status 'Delivered' or 'Shipped' and type 'New Order' were considered.
                    """)
        df = pd.read_csv(product_file[0])

        df['payout_total_values'] = df['payout_total_values']/100

        # Convert 'brand_contacted_at_values' to datetime
        df['brand_contacted_at_values'] = pd.to_datetime(df['brand_contacted_at_values'], unit='ms')

        # Filter orders where creation_reasons is equal to NEW_ORDER
        df = df[(df['creation_reasons'] == 'NEW_ORDER') & ((df['states'] == 'SHIPPED') | (df['states'] == 'DELIVERED'))]

        lifetime_performance_metrics(df, date_last_update)

        sales_per_quarter(df)

        sales_previous_year_vs_sales_year_before_that_one(df, date_last_update)

        orders_previous_year_vs_orders_year_before_that_one(df, date_last_update)

        sales_by_source(df, date_last_update)

        new_merchants_by_source(df, date_last_update)

        #type_of_store_top_10_retailers(df, date_last_update)

        #sales_distribution(df, date_last_update)

    elif selected_report == "Competitors analytics":
        
        create_competitors_dashboard(selected_client, markdown_text)
    
    elif selected_report == "Custom Competitors analytics":
        
        create_custom_competitors_dashboard(selected_client, markdown_text)
        