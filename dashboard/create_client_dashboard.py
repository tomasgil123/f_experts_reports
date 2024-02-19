import streamlit as st
import pandas as pd
import glob
import os

def list_files_in_directory(directory_path):
    with os.scandir(directory_path) as entries:
        for entry in entries:
            print(entry.name)

from dashboard.product_analytics_charts import (generate_pageviews_orders_ratio_chart, 
                    generate_page_views_chart_by_category,
                    generate_page_views_chart_by_product, 
                    generate_page_views_and_ratio_by_category_with_selector, 
                    generate_page_views_orders_ratio_chart_by_category,
                    generate_page_views_and_ratio_by_product_with_selector)

from dashboard.order_analytics_charts import (lifetime_performance_metrics, sales_per_quarter, 
                                    sales_previous_year_vs_sales_year_before_that_one,
                                    orders_previous_year_vs_orders_year_before_that_one, sales_by_source,
                                    new_merchants_by_source)

from dashboard.competitors_analytics_charts import (
                                          get_competitors_total_reviews,
                                          get_competitors_average_rating,
                                          get_competitors_reviews_by_month,
                                          get_competitors_most_common_words_in_reviews, 
                                          get_competitors_most_common_words_title, 
                                          get_competitors_price_distribution_by_category,
                                          get_competitors_minimum_order_data,
                                          get_competitors_fulfillment_data,
                                          get_number_collections_per_brand,
                                          get_median_maturity_collections_per_brand,
                                          get_median_update_time_collections_per_brand,
                                          get_median_items_per_collection_per_brand)

from dashboard.email_marketing_analytics_charts import (get_email_marketing_kpis_last_30_days, 
                                              get_email_marketing_kpis_by_month, sales_by_month)

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


def create_dashboard(selected_client, selected_report):

    markdown_text = read_md_file(f"./dashboard/dashboard_text/{selected_client}/texts.md")
    
    if selected_report == "Email marketing analytics":
        data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/marketing_campaign_info.csv")

        get_email_marketing_kpis_last_30_days(data)

        get_email_marketing_kpis_by_month(data)

        sales_by_month(data, 'open_based_total_order_value', 'Total Sales Open emails (12 months)')
        sales_by_month(data, 'click_based_total_order_value', 'Total Sales Click emails (12 months)')

    elif selected_report == "Product analytics":
        data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/product_analytics.csv")

        data['Date'] = pd.to_datetime(data['Date'])

        st.title("Product Analytics Dashboard")

        generate_page_views_chart_by_category(data, 2023)

        generate_page_views_chart_by_product(data, 2023)

        generate_page_views_orders_ratio_chart_by_category(data, 2023)

        generate_pageviews_orders_ratio_chart(data, 2023)

        generate_page_views_and_ratio_by_category_with_selector(data)

        generate_page_views_and_ratio_by_product_with_selector(data)

    elif selected_report == "Order analytics":
        st.markdown("""
                    # Order Analytics Dashboard
                    ### Total sales, average order value and orders
                    Only orders with status 'Delivered' or 'Shipped' were considered.
                    """)
        df = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/orders_from_api.csv")
        df['payout_total_values'] = df['payout_total_values']/100

        lifetime_performance_metrics(df)

        sales_per_quarter(df)

        sales_previous_year_vs_sales_year_before_that_one(df)

        orders_previous_year_vs_orders_year_before_that_one(df)

        sales_by_source(df)

        new_merchants_by_source(df)

    elif selected_report == "Competitors analytics":
        df_brand_data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/brand_info.csv")

        product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/competitors_data/products_*.csv")


        df = pd.read_csv(product_file[0])
        df_reviews = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/reviews.csv")

        st.markdown("""
                    # Competitors analytics dashboard
                    #### Review analysis:
                    ###
                    """)
        get_competitors_total_reviews(df_reviews)

        get_competitors_average_rating(df_reviews)

        get_competitors_reviews_by_month(df_reviews)

        get_competitors_most_common_words_in_reviews(df_reviews)

        review_analysis = get_text_between_comments(markdown_text, "<!-- Review analysis -->", "<!")
        if review_analysis is not None:
            st.markdown(review_analysis, unsafe_allow_html=True)

        st.markdown("""
                    #### Product analysis:
                    ###
                    """)
        get_competitors_most_common_words_title(df)
        
        product_optimization_strategies = get_text_between_comments(markdown_text, "<!-- Product optimization analysis -->", "<!")
        if product_optimization_strategies is not None:
            st.markdown(product_optimization_strategies, unsafe_allow_html=True)

        st.markdown("""
                    #### Pricing, minimum order and fulfillment analysis:
                    ###
                    """)
        get_competitors_price_distribution_by_category(df)

        get_competitors_minimum_order_data(df_brand_data)

        get_competitors_fulfillment_data(df_brand_data)

        pricing_strategy = get_text_between_comments(markdown_text, "<!-- Competitor pricing, minimum order and fulfillment analysis -->", "<!")
        if pricing_strategy is not None:
            st.markdown(pricing_strategy, unsafe_allow_html=True)

        st.markdown("""
                    #### Collections analysis:
                    ###
                    """)

        df_brands_collections = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/collections.csv")

        get_number_collections_per_brand(df_brands_collections)

        get_median_maturity_collections_per_brand(df_brands_collections)

        get_median_update_time_collections_per_brand(df_brands_collections)

        get_median_items_per_collection_per_brand(df_brands_collections)

        collections = get_text_between_comments(markdown_text, "<!-- Competitor collection analysis -->", "<!")
        if collections is not None:
            st.markdown(collections, unsafe_allow_html=True)

        