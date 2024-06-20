import streamlit as st
import pandas as pd
import glob
import numpy as np

from dashboard.competitors_analytics_charts import (
                                          get_competitors_total_reviews,
                                          get_competitors_average_rating,
                                          get_brands_total_reviews,
                                          get_brands_average_rating,
                                          get_competitors_reviews_by_month,
                                          get_competitors_most_common_words_in_reviews, 
                                          get_competitors_most_common_words_title_data,
                                          get_competitors_most_common_words_title_display, 
                                          get_competitors_price_distribution_by_category_data,
                                          get_competitors_price_distribution_by_category_display,
                                          get_competitors_price_distribution_by_category_display_custom,
                                          get_competitors_price_table_data,
                                          get_competitors_price_table_display,
                                          get_competitors_minimum_order_data,
                                          get_competitors_fulfillment_data,
                                          get_number_collections_per_brand,
                                          get_median_maturity_collections_per_brand,
                                          get_median_update_time_collections_per_brand,
                                          get_median_items_per_collection_per_brand,
                                          get_badge_items_per_category,
                                          display_product_links)

from dashboard.utils import (extract_date_from_filename, get_text_between_comments)

from dashboard.utils_llm import OpenaiInsights

def create_competitors_dashboard(selected_client, markdown_text):

    insights = OpenaiInsights()  

    df_brand_data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/brand_info.csv")

    product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/competitors_data/products_*.csv")

    date_last_update = extract_date_from_filename(product_file[0])

    st.write(f"Data was last updated at: {date_last_update.date()}")

    df = pd.read_csv(product_file[0])
    df_reviews = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/reviews.csv")

    st.markdown("""
                # Competitors analytics
                """)
    
    if selected_client == "teleties":
        st.markdown("""
                    Competitors were selected based on their presence in the Hair Claws and Clips category, which accounts for the majority of Teleties' sales.
                    """)
    
    st.markdown("""
                #### Review analysis:
                """)
    
    review_analysis = get_text_between_comments(markdown_text, "<!-- Competitors: Review analysis -->", "<!")
    if review_analysis is not None:
        st.markdown(review_analysis, unsafe_allow_html=True)
        
    get_competitors_total_reviews(df_reviews)

    get_competitors_average_rating(df_reviews)

    get_competitors_reviews_by_month(df_reviews)

    get_competitors_most_common_words_in_reviews(df_reviews)

    st.markdown("""
                #### Product analysis:
                """)
    
    product_optimization_strategies = get_text_between_comments(markdown_text, "<!-- Competitors: Product optimization analysis -->", "<!")
    if product_optimization_strategies is not None:
        st.markdown(product_optimization_strategies, unsafe_allow_html=True)
    
    all_brands_option = "All Brands"

    # Create a brand selector widget
    selected_brand = st.selectbox("Select a Brand", np.append(df['brand'].unique(), all_brands_option))
    # Create a product category selector widget
    selected_category = st.selectbox("Select a Product Category", df['Product Category'].unique())

    df_product_names = get_competitors_most_common_words_title_data(df, selected_brand, selected_category)

    get_competitors_most_common_words_title_display(df_product_names, selected_brand, selected_category)

    if st.session_state.get("is_admin", True): 
        st.dataframe(df_product_names)
        string_dataframe = df_product_names.to_string(index=False)
        insights.display_llm_insight_helper({"string_data": string_dataframe, "section": "<!-- Competitors: Product titles analysis -->", "button_key": "df_product_names"})
    
    

    st.markdown("""
                #### Pricing, minimum order and fulfillment analysis:
                """)
    
    pricing_strategy = get_text_between_comments(markdown_text, "<!-- Competitors: Competitor pricing, minimum order and fulfillment analysis -->", "<!")
    if pricing_strategy is not None:
        st.markdown(pricing_strategy, unsafe_allow_html=True)
    
    all_brands_option = "All Brands"
    
    selected_brand = st.selectbox("Select Brand", np.append(df['brand'].unique(), all_brands_option))
    selected_category = st.selectbox("Select Category", df['Product Category'].unique(), index=0)

    # we replace "_" with " " in selected_brand and also we make the first leeter of each word upper case
    name_selected_client = selected_client.replace("_", " ").title()

    df_competitors_price_distribution = get_competitors_price_distribution_by_category_data(df, selected_brand, all_brands_option, selected_category)
    get_competitors_price_distribution_by_category_display(df_competitors_price_distribution,selected_category, selected_brand, client=name_selected_client)

    df_sum_data = get_competitors_price_table_data(df, selected_category)
    get_competitors_price_table_display(df_sum_data, selected_category)

    if st.session_state.get("is_admin", True):
        st.dataframe(df_competitors_price_distribution)
        string_dataframe = df_sum_data.to_string(index=False)
        insights.display_llm_insight_helper({"string_data": string_dataframe, "section": "<!-- Competitors: Prices analysis -->", "button_key": "df_competitors_price_distribution"})

    get_competitors_minimum_order_data(df_brand_data)

    get_competitors_fulfillment_data(df_brand_data)

    

    st.markdown("""
                #### Collections analysis:
                """)

    collections = get_text_between_comments(markdown_text, "<!-- Competitors: Competitor collection analysis -->", "<!")
    if collections is not None:
        st.markdown(collections, unsafe_allow_html=True)

    df_brands_collections = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/collections.csv")

    get_number_collections_per_brand(df_brands_collections)

    get_median_maturity_collections_per_brand(df_brands_collections)

    get_median_update_time_collections_per_brand(df_brands_collections)

    get_median_items_per_collection_per_brand(df_brands_collections)
    

def create_custom_competitors_dashboard(selected_client, markdown_text):
    
    df_brand_data = pd.read_csv(f"./dashboard/dashboard_data/{selected_client}/competitors_data/custom_brand_info.csv")

    product_file = glob.glob(f"./dashboard/dashboard_data/{selected_client}/competitors_data/custom_products_*.csv")

    date_last_update = extract_date_from_filename(product_file[0])
    st.write(f"Data was last updated at: {date_last_update.date()}")

    df_product_data = pd.read_csv(product_file[0])
    

    st.markdown("""
                # Competitors analytics
                #### Review analysis:
                ###
                """)
    # Get unique categories
    categories = df_product_data["Product Category"].unique()

    # Allow user to select multiple categories
    selected_categories = st.multiselect("Select Categories", categories)

    if not selected_categories:
        filtered_brands = df_brand_data
    else:
        # Filter products DataFrame based on selected categories
        filtered_products = df_product_data[df_product_data["Product Category"].isin(selected_categories)]

        # Get unique brands associated with selected categories
        brands_in_selected_categories = filtered_products["Brand ID"].unique()

        # Filter brands DataFrame based on brands associated with selected categories
        filtered_brands = df_brand_data[df_brand_data["Brand Token"].isin(brands_in_selected_categories)]
    
    get_brands_total_reviews(filtered_brands)

    get_brands_average_rating(filtered_brands)
    
    st.markdown("""
                #### Pricing analysis:
                ###
                """)
    # we add column "brand" to df_product_data from df_brand_data
    df_product_data = df_product_data.merge(df_brand_data[['Brand Token', 'Brand Name']], left_on="Brand ID", right_on="Brand Token")
    # we rename new column "Brand Name" to "brand"
    df_product_data.rename(columns={"Brand Name": "brand"}, inplace=True)
    
    all_brands_option = "All Brands"
    
    selected_brand = st.selectbox("Select Brand", np.append(df_product_data['brand'].unique(), all_brands_option))
    selected_category = st.selectbox("Select Category", df_product_data['Product Category'].unique(), index=0)

    df_competitors_price_distribution = get_competitors_price_distribution_by_category_data(df_product_data, selected_brand, all_brands_option, selected_category)
    get_competitors_price_distribution_by_category_display_custom(df_competitors_price_distribution,selected_category, selected_brand, client=selected_client )

    df_sum_data = get_competitors_price_table_data(df_product_data, selected_category)
    get_competitors_price_table_display(df_sum_data, selected_category)

    pricing_analysis = get_text_between_comments(markdown_text, "<!-- Custom Competitors: Competitor pricing -->", "<!")
    if pricing_analysis is not None:
        st.markdown(pricing_analysis, unsafe_allow_html=True)
    
    st.markdown("""
                #### Minimum order and fulfillment analysis:
                ###
                """)
    
    get_competitors_minimum_order_data(df_brand_data)

    get_competitors_fulfillment_data(df_brand_data)
    
    st.markdown("""
                #### Best selling, new arrivals and promos analysis:
                ###
                """)
    
    st.markdown(""" 
        ##### Bestseller: 
        Have the highest repeat sales in their category on Faire.
                
        ##### Trending: 
        Faire labels some product, but it is not clear how they measure it. Probably has to do with page views. 
    """)
    
    selected_category = st.selectbox("Select Category", df_product_data['Product Category'].unique(), key="type_badge")

    # How many best selling products has each competitor for a specific category? This way we know who is leading the category
    title_bestseller = f"Top 10 Brands with Most Bestseller Products in {selected_category}"
    get_badge_items_per_category(df_product_data, "FAIRE_BESTSELLER", selected_category, title=title_bestseller)

    display_product_links(df_product_data, "FAIRE_BESTSELLER", selected_category)

    # How many new products each category has? who is providing them?
    title_new = f"Top 10 Brands with Most New Products in {selected_category}"
    get_badge_items_per_category(df_product_data, "NEW_BADGE", selected_category, title=title_new)

    display_product_links(df_product_data, "NEW_BADGE", selected_category)

    # How many trending products each category has? who is providing them?
    title_trending = f"Top 10 Brands with Most Trending Products in {selected_category}"
    get_badge_items_per_category(df_product_data, "TRENDING", selected_category, title=title_trending)

    display_product_links(df_product_data, "TRENDING", selected_category)

    # How many products have discount? who is providing them?  