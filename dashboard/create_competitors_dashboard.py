import streamlit as st
import pandas as pd
import glob
import numpy as np

from dashboard.competitors_analytics_charts import (
                                          get_competitors_total_reviews,
                                          get_competitors_average_rating,
                                          get_competitors_reviews_by_month,
                                          get_competitors_most_common_words_in_reviews, 
                                          get_competitors_most_common_words_title_data,
                                          get_competitors_most_common_words_title_display, 
                                          get_competitors_price_distribution_by_category,
                                          get_competitors_minimum_order_data,
                                          get_competitors_fulfillment_data,
                                          get_number_collections_per_brand,
                                          get_median_maturity_collections_per_brand,
                                          get_median_update_time_collections_per_brand,
                                          get_median_items_per_collection_per_brand)

from dashboard.utils import (extract_date_from_filename, get_text_between_comments)

from dashboard.utils_llm import OpenaiInsights

def create_competitors_dashboard(selected_client, markdown_text):  

    df_brand_data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/brand_info.csv")

    product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/competitors_data/products_*.csv")

    date_last_update = extract_date_from_filename(product_file[0])

    st.write(f"Data was last updated at: {date_last_update.date()}")

    df = pd.read_csv(product_file[0])
    df_reviews = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/reviews.csv")

    st.markdown("""
                # Competitors analytics
                #### Review analysis:
                ###
                """)
        
    get_competitors_total_reviews(df_reviews)

    get_competitors_average_rating(df_reviews)

    get_competitors_reviews_by_month(df_reviews)

    get_competitors_most_common_words_in_reviews(df_reviews)

    review_analysis = get_text_between_comments(markdown_text, "<!-- Competitors: Review analysis -->", "<!")
    if review_analysis is not None:
        st.markdown(review_analysis, unsafe_allow_html=True)

    st.markdown("""
                #### Product analysis:
                ###
                """)
    
    all_brands_option = "All Brands"
    # Create a brand selector widget
    selected_brand = st.selectbox("Select a Brand", np.append(df['brand'].unique(), all_brands_option))
    # Create a product category selector widget
    selected_category = st.selectbox("Select a Product Category", df['Product Category'].unique())

    df_product_names = get_competitors_most_common_words_title_data(df, selected_brand, selected_category)

    get_competitors_most_common_words_title_display(df_product_names, selected_brand, selected_category)

    if st.session_state.get("is_admin", True): 
        insights = OpenaiInsights() 
        st.dataframe(df_product_names)
        string_dataframe = df_product_names.to_string(index=False)
        insights.display_llm_insight_helper({"string_data": string_dataframe, "section": "<!-- Competitors: Product titles analysis -->"})
    
    product_optimization_strategies = get_text_between_comments(markdown_text, "<!-- Competitors: Product optimization analysis -->", "<!")
    if product_optimization_strategies is not None:
        st.markdown(product_optimization_strategies, unsafe_allow_html=True)

    st.markdown("""
                #### Pricing, minimum order and fulfillment analysis:
                ###
                """)
    get_competitors_price_distribution_by_category(df)

    get_competitors_minimum_order_data(df_brand_data)

    get_competitors_fulfillment_data(df_brand_data)

    pricing_strategy = get_text_between_comments(markdown_text, "<!-- Competitors: Competitor pricing, minimum order and fulfillment analysis -->", "<!")
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

    collections = get_text_between_comments(markdown_text, "<!-- Competitors: Competitor collection analysis -->", "<!")
    if collections is not None:
        st.markdown(collections, unsafe_allow_html=True)