import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from product_analytics_charts import (generate_pageviews_orders_ratio_chart, 
                    generate_page_views_chart_by_category,
                    generate_page_views_chart_by_product, 
                    generate_page_views_and_ratio_by_category_with_selector, 
                    generate_page_views_orders_ratio_chart_by_category,
                    generate_page_views_and_ratio_by_product_with_selector)

from order_analytics_charts import (lifetime_performance_metrics)

from competitors_analytics_charts import (get_competitors_brand_data,
                                          get_competitors_total_reviews,
                                          get_competitors_average_rating,
                                          get_competitors_reviews_by_month,
                                          get_competitors_most_common_words_in_reviews, 
                                          get_competitors_most_common_words_title, 
                                          get_competitors_price_distribution_by_category,
                                          get_competitors_minimum_order_data,
                                          get_competitors_fulfillment_data)


with open("custom.css") as f:
    custom_css = f.read()

# Use st.markdown to inject the CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

options = ["Product analytics", "Order analytics", "Competitors analytics"]

default_option = "Competitors analytics"

selected_option = st.sidebar.radio("Select an Option", options, index=options.index(default_option))


# Depending on the selected option, display corresponding charts
if selected_option == "Product analytics":
    # Load the CSV data
    data = pd.read_csv('product_analytics.csv')

    # Convert 'Date' column to datetime
    data['Date'] = pd.to_datetime(data['Date'])

    # Create a Streamlit app
    st.title("Product Analytics Dashboard")

    generate_page_views_chart_by_category(data, 2023)

    generate_page_views_chart_by_product(data, 2023)

    generate_page_views_orders_ratio_chart_by_category(data, 2023)

    generate_pageviews_orders_ratio_chart(data, 2023)

    generate_page_views_and_ratio_by_category_with_selector(data)

    generate_page_views_and_ratio_by_product_with_selector(data)
elif selected_option == "Order analytics":
    st.markdown("<div id='start' ></div>", unsafe_allow_html=True)
    st.title("Order Analytics Dashboard")

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('faire_orders.csv')

    # Convert the "Order Date" column to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%B %d, %Y')
    df['Wholesale Price'] = df['Wholesale Price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

    lifetime_performance_metrics(df)
    st.markdown("<div id='end' ></div>", unsafe_allow_html=True)

elif selected_option == "Competitors analytics":
    
    df_brand_data = get_competitors_brand_data()

    df = pd.read_csv('competitors_data/products_20240130.csv')
    df_reviews = pd.read_csv('competitors_data/reviews.csv')
    
    st.markdown("""
                # Competitors Analytics Dashboard
                ### Review Analysis:
                ###
                """)
    get_competitors_total_reviews(df_reviews)

    get_competitors_average_rating(df_reviews)

    get_competitors_reviews_by_month(df_reviews)

    get_competitors_most_common_words_in_reviews(df_reviews)

    st.markdown("""
                #

                General Trends: Most competitors have over 30 reviews.

                Notable Exception: Threaded Pair stands out with over 450 reviews.

                Rating Overview: All competitors maintain high ratings, averaging above 4.8 stars.

                #
                """, unsafe_allow_html=True)

    st.markdown("""
                #### Product Optimization Strategies:
                ###
                """)
    get_competitors_most_common_words_title(df)

    st.markdown("""
                # 

                Enhance Product Titles: Incorporate ‘Handcrafted’ into product names to emphasize craftsmanship. 

                Highlight Media Recognition: Showcase publications where Latico has been featured, enhancing brand credibility. 

                Leverage Awards: Use ‘award-winning’ in product descriptions to underline quality and distinction. 

                Seasonal Marketing Focus: Utilize holiday-themed keywords in collection names, email campaign subjects, and content to drive seasonal sales.
                
                # 

                """, unsafe_allow_html=True)

    st.markdown("""
                #### Key marketing insights:
                ###
                """)
    get_competitors_price_distribution_by_category(df)
    st.markdown("""
                ##### Pricing strategy:

                Competitors generally offer products at a lower price point, likely making them more accessible to a wider audience.
                
                ##### Suggestion:
                
                Consider revising Latico’s pricing strategy to be more competitive, particularly for entry-level products.
                
                """, unsafe_allow_html=True)

    get_competitors_minimum_order_data(df_brand_data)
    st.markdown("""
                # 

                Brand Minimums: Latico’s current minimum order value is significantly higher (\$500) compared to competitors, who range between \$100-\$300. 

                Recommendation: Lower the minimum order value to align more closely with market standards. This could enhance accessibility and appeal to a broader customer base.

                #
                """, unsafe_allow_html=True)

    get_competitors_fulfillment_data(df_brand_data)



