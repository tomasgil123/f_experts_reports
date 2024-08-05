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
                                    type_of_store_top_10_retailers, sales_distribution, 
                                    sales_quantiles, purchase_frequency, retailers_did_not_reorder, 
                                    sales_by_store_type, sales_by_category, avg_order_value_by_store_type, get_cold_outreach_lead_sales,
                                    display_insider_info, get_top_products)


from dashboard.email_marketing_analytics_charts import (get_email_marketing_kpis_last_30_days, 
                                              get_email_marketing_kpis_by_month, sales_by_month)

from dashboard.utils import (extract_date_from_filename, read_md_file, get_text_between_comments,
                              save_user_log_report, get_data_from_google_spreadsheet, snake_to_title, get_orders_teleties, get_orders_items_teleties)

from dashboard.seo_analytics_charts import (get_brands_with_most_products_in_top_100, get_evolution_rankings_products_given_query)

# Dashboard creation
from dashboard.create_competitors_dashboard import (create_competitors_dashboard, create_custom_competitors_dashboard)


def create_dashboard(selected_client, selected_report, is_admin):

    # if is admin is false, we save log
    if not is_admin:
        save_user_log_report(selected_client, selected_report)

    markdown_text = read_md_file(f"./dashboard/dashboard_text/{selected_client}/texts.md")

    if selected_report == "SEO":
        st.markdown("""
                # SEO
                ### SEO performance review
                """)
        spreadsheet_id = '1yN0KXGaGTBIjx9VwRAc-ce9WS6dBgwSel1Jf7qWiInA'  # Please set the Spreadsheet ID.
        range_name = 'Main'  # Example sheet name
        df_queries = get_data_from_google_spreadsheet(spreadsheet_id, range_name)

        df_queries_brand = df_queries[df_queries['Brand'] == snake_to_title(selected_client)]

        query_selected = st.selectbox('Select a query', df_queries_brand['Query'].unique())

        # we load seo_rankings csv file data
        df_seo = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/seo_rankings.csv")
        df_seo_top_10 = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/seo_rankings_top_10.csv")

        get_evolution_rankings_products_given_query(df=df_seo, query=query_selected)

        get_evolution_rankings_products_given_query(df=df_seo_top_10, query=query_selected)
    
    if selected_report == "Email marketing analytics":

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/marketing_campaign_info_*.csv")

        date_last_update = extract_date_from_filename(product_file[0])

        st.write(f"Data was last updated at: {date_last_update.date()}")

        data = pd.read_csv(product_file[0])

        df_marketing_campaigns_completed = data[data['states'] == 'COMPLETED']

        # if dataframe is empty

        if df_marketing_campaigns_completed.empty:
            st.markdown("""
                # Email Marketing Analytics
                There is no email marketing data available. No email campaigns have been marked as 'completed'.
                """)
        else:

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

            

            if selected_client == 'teleties':
                df_orders = get_orders_teleties()
                date_last_update_orders = "2024-08-05"
                date_last_update_orders = datetime.strptime(date_last_update_orders, '%Y-%m-%d')
            else:
                df_orders = pd.read_csv(product_file_orders[0])
                date_last_update_orders = extract_date_from_filename(product_file_orders[0])

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

            # dont display this section if client is be_huppy
            if selected_client != "be_huppy":
                st.markdown("""
                            #
                        #### Store type campaigns
                        """)
                
                
                type_store_campaigns = get_text_between_comments(markdown_text, "<!-- Email marketing: Campaign ideas type store -->", "<!")
                if type_store_campaigns is not None:
                    st.markdown(type_store_campaigns, unsafe_allow_html=True)
                
                product_file_items_orders = glob.glob(f"./dashboard/dashboard_data/{selected_client}/items_order_from_api_*.csv")

                if selected_client == 'teleties':
                    df_order_items = get_orders_items_teleties()
                else:
                    df_order_items = pd.read_csv(product_file_items_orders[0])

                product_file_items_page_views = glob.glob(f"./dashboard/dashboard_data/{selected_client}/page_views_info_*.csv")
                df_page_views = pd.read_csv(product_file_items_page_views[0])

                sales_by_store_type(df_orders, df_order_items, df_page_views)

    elif selected_report == "Product analytics":

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/page_views_info_*.csv")

        date_last_update = extract_date_from_filename(product_file[0])

        st.write(f"Data was last updated at: {date_last_update.date()}")

        data = pd.read_csv(product_file[0])

        def preprocess_date(date):
            if ' ' in date:
                return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').strftime('%Y/%m/%d')
            else:
                return datetime.strptime(date, '%Y-%m-%d').strftime('%Y/%m/%d')

        data['date'] = data['date'].apply(preprocess_date)

        data['date'] = pd.to_datetime(data['date'])

        st.markdown(f"# Product Analytics")

        page_views_by_category_analysis = get_text_between_comments(markdown_text, "<!-- Product: page views by category last 12 months -->", "<!")
        if page_views_by_category_analysis is not None:
            st.markdown(page_views_by_category_analysis, unsafe_allow_html=True)

        if selected_client == "jack_archer":
            return

        generate_page_views_chart_by_category_last_12_months(data, date_last_update)

        generate_page_views_evolution_last_12_months_by_category(data)

        # generate_page_views_chart_by_product_last_12_months(data, date_last_update)
            
        # generates_sales_chart_by_category_last_12_months(data, date_last_update)

        # if columns sales_count and orders_count sum cero, don't display the following charts
        if data['sales_count'].sum() != 0 and data['order_count'].sum() != 0:

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

        if selected_client == 'teleties':
            df = get_orders_teleties()
            date_last_update_orders = "2024-08-05"
            date_last_update = datetime.strptime(date_last_update_orders, '%Y-%m-%d')
            st.write(f"Data was last updated at: {date_last_update.date()}")
        else:
            date_last_update = extract_date_from_filename(product_file[0])
            st.write(f"Data was last updated at: {date_last_update.date()}")
            df = pd.read_csv(product_file[0])
        
        if df.empty:
            st.markdown("""
                    # Order Analytics
                    There is no orders data available.
                    """)
            return
        
        st.markdown("""
                    # Order Analytics
                    ### Total sales, average order value and orders
                    Only orders with status 'Delivered' or 'Shipped' and type 'New Order' were considered.
                    """)
        
        df['payout_total_values'] = df['payout_total_values']/100

        # Convert 'brand_contacted_at_values' to datetime
        df['brand_contacted_at_values'] = pd.to_datetime(df['brand_contacted_at_values'], unit='ms')

        # Filter orders where creation_reasons is equal to NEW_ORDER
        df = df[(df['creation_reasons'] == 'NEW_ORDER') & ((df['states'] == 'SHIPPED') | (df['states'] == 'DELIVERED'))]

        product_file_items_orders = glob.glob(f"./dashboard/dashboard_data/{selected_client}/items_order_from_api_*.csv")
        
        if selected_client == 'teleties':
            df_order_items = get_orders_items_teleties()
        else:
            df_order_items = pd.read_csv(product_file_items_orders[0])

        product_file_page_views = glob.glob(f"./dashboard/dashboard_data/{selected_client}/page_views_info_*.csv")
        df_page_views = pd.read_csv(product_file_page_views[0])

        lifetime_performance_metrics(df, date_last_update)

        sales_per_quarter(df)

        sales_previous_year_vs_sales_year_before_that_one(df, date_last_update)

        orders_previous_year_vs_orders_year_before_that_one(df, date_last_update)

        sales_by_source(df, date_last_update)

        new_merchants_by_source(df, date_last_update)

        sales_by_category(df, df_order_items, df_page_views)

        get_top_products(df_order_items, df)

        avg_order_value_by_store_type(df, day_data_was_obtained=date_last_update)

        # type_of_store_top_10_retailers(df, date_last_update)

        # if dataframe includes colum "is_insider" we display the following charts
        if 'is_insider' in df.columns:
            st.markdown("""
                        ### Insider customers
                        """)
            display_insider_info(df)
                    
        # sales_distribution(df, date_last_update)
        if is_admin:
            st.markdown("""
                        ### Cold outreach results
                        """)
            selected_client_formatted = selected_client.replace('_', ' ').title()
            get_cold_outreach_lead_sales(df_orders=df, selected_client=selected_client_formatted)

    elif selected_report == "Competitors analytics":
        
        create_competitors_dashboard(selected_client, markdown_text)
    
    elif selected_report == "Custom Competitors analytics":
        
        create_custom_competitors_dashboard(selected_client, markdown_text)
        