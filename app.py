import streamlit as st
import pandas as pd

from product_analytics_charts import (generate_pageviews_orders_ratio_chart, 
                    generate_page_views_chart_by_category,
                    generate_page_views_chart_by_product, 
                    generate_page_views_and_ratio_by_category_with_selector, 
                    generate_page_views_orders_ratio_chart_by_category,
                    generate_page_views_and_ratio_by_product_with_selector)

from order_analytics_charts import (lifetime_performance_metrics)

with open("custom.css") as f:
    custom_css = f.read()

# Use st.markdown to inject the CSS
st.markdown(f'<style>{custom_css}</style>', unsafe_allow_html=True)

options = ["Product analytics", "Order analytics", "Competitors analytics"]

default_option = "Order analytics"

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
    st.title("Order Analytics Dashboard")

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv('faire_orders.csv')

    # Convert the "Order Date" column to datetime
    df['Order Date'] = pd.to_datetime(df['Order Date'], format='%B %d, %Y')
    df['Wholesale Price'] = df['Wholesale Price'].str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)

    lifetime_performance_metrics(df)

elif selected_option == "Competitors analytics":
    st.title("Competitors Analytics Dashboard")


