import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_page_views_chart_by_category(data, year):
    st.markdown("<h1 class='title-text'>Total Page Views by Product Type for year 2023</h1>", unsafe_allow_html=True)
    # Group the data by the 'Type' column and calculate the sum of 'Page views'
    category_views_2023 = data[data['Date'].dt.year == year].groupby('Type')['Page views'].sum().reset_index()

    # Sort the DataFrame by 'Page views' in descending order
    category_views_2023 = category_views_2023.sort_values(by='Page views', ascending=False)

    # Create a bar chart using matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(category_views_2023['Type'], category_views_2023['Page views'])
    plt.xlabel('Product Category')
    plt.ylabel('Total Page Views')
    plt.xticks(rotation=45, ha='right')

    # Display the chart in your Streamlit app
    st.pyplot(plt)

    st.markdown("<p class='body-text'>Cross body bag and tote bag are by far the types that most page views generate. There are several categories that generate almost no views.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold;' class='body-text'>Opportunity</p>", unsafe_allow_html=True)
    st.markdown("<p class='body-text'>Do SEO for type of products with few page views and low page views / ratio (or in other words high conversion). For example: 'wristlet'.</p>", unsafe_allow_html=True)


def generate_page_views_chart_by_product(data_original, year):
    st.markdown("<h1 class='title-text'>Total Page Views by Product for year 2023</h1>", unsafe_allow_html=True)

    data = data_original.copy()
    default_value = "Crossbody Bags"  # Replace with the name you want as the default

    options = data['Type'].unique()
    default_index = options.tolist().index(default_value)

    selected_type = st.selectbox(
        "Select Product Type",
        options,
        key="generate_page_views_chart_by_product",
        index=default_index
    )
    # Group the data by the 'Type' column and calculate the sum of 'Page views'
    product_views_2023 = data[(data['Date'].dt.year == year) & (data['Type'] == selected_type)].groupby('Product name')['Page views'].sum().reset_index()
    
    # Sort the DataFrame by 'Page views' in descending order
    product_views_2023 = product_views_2023.sort_values(by='Page views', ascending=False)
    filtered_products = product_views_2023.head(12)

    # Create a bar chart using matplotlib
    plt.figure(figsize=(10, 6))
    plt.bar(filtered_products['Product name'], filtered_products['Page views'])
    plt.xlabel('Product Category')
    plt.ylabel('Total Page Views')
    plt.xticks(rotation=45, ha='right')

    # Display the chart in your Streamlit app
    st.pyplot(plt)

def generate_page_views_orders_ratio_chart_by_category(data_original, year):
    st.markdown("<h1 class='title-text'>Page Views / Orders Ratio by Product Type (Descending Order, >= 500 Total Views)</h1>", unsafe_allow_html=True)

    data = data_original.copy()
    # Calculate the total page views for each product
    total_page_views = data[data['Date'].dt.year == year].groupby('Type')['Page views'].sum().reset_index()

    # Filter products with at least 500 total page views
    filtered_categories = total_page_views[total_page_views['Page views'] >= 500]['Type']

    # Filter the original data to keep only the selected categories
    filtered_data = data[data['Type'].isin(filtered_categories)]

    # Group the filtered data by the 'Type' column and calculate the sum of 'Page views' and 'Orders'
    category_views_orders = filtered_data.groupby('Type')[['Page views', 'Orders']].sum().reset_index()

    # Calculate the ratio of Page views to Orders
    category_views_orders['PageViews/Orders Ratio'] = category_views_orders['Page views'] / category_views_orders['Orders']

    # Sort the DataFrame by the ratio in descending order
    category_views_orders = category_views_orders.sort_values(by='PageViews/Orders Ratio', ascending=True)

    # Create a bar chart using matplotlib
    plt.figure(figsize=(10, 6))

    plt.bar(category_views_orders['Type'], category_views_orders['PageViews/Orders Ratio'])
    plt.xlabel('Product Category')
    plt.ylabel('Page Views / Orders Ratio')
    plt.xticks(rotation=45, ha='right')

    # Display the chart in your Streamlit app
    st.pyplot(plt)

    st.markdown("<p class='body-text'>Page views / orders ratio is different across type of products. The best converting type is 'Wristlet'. Every 8-9 page views an order is placed.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold;' class='body-text'>Opportunity</p>", unsafe_allow_html=True)
    st.markdown("<p class='body-text'>'Wristlet' has low page views, but very good conversion rate. It might be worth to grab the best performing products in the category and improve product title, description, tags, etc in order to increment page views.</p>", unsafe_allow_html=True)


def generate_pageviews_orders_ratio_chart(data_original, year):
    st.markdown("<h1 class='title-text'>Page Views / Orders Ratio by Product (Descending Order, first 12 products with most views)</h1>", unsafe_allow_html=True)

    data = data_original.copy()
    data_year = data[data['Date'].dt.year == year]

    default_value = "Crossbody Bags"  # Replace with the name you want as the default

    options = data['Type'].unique()
    default_index = options.tolist().index(default_value)

    selected_type = st.selectbox(
        "Select Product Type",
        options,
        key="generate_pageviews_orders_ratio_chart",
        index=default_index
    )

    # Calculate the total page views for each product
    total_page_views = data_year[data_year['Type'] == selected_type].groupby('Product name')['Page views'].sum().reset_index()

    # Sort the products by Page views in descending order
    total_page_views = total_page_views.sort_values(by='Page views', ascending=False)

    # Keep only the top 12 products
    filtered_products = total_page_views.head(12)['Product name']

    # Filter the original data to keep only the selected products
    filtered_data = data_year[data_year['Product name'].isin(filtered_products) & (data_year['Type'] == selected_type)]
    # Group by 'Product name' and aggregate the sum of 'Page views', 'Orders', and 'Units sold'
    grouped_df = filtered_data.groupby('Product name').agg({
        'Page views': 'sum',
        'Orders': 'sum',
        'Units sold': 'sum'
    }).reset_index()

    # Calculate the ratio of Page views to Orders
    grouped_df['PageViews/Orders Ratio'] = grouped_df['Page views'] / grouped_df['Orders']

    # Sort the DataFrame by the ratio in descending order
    grouped_df = grouped_df.sort_values(by='PageViews/Orders Ratio', ascending=True)

     # Create the Matplotlib chart
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot 'Page views' on the primary y-axis
    ax1.bar( grouped_df['Product name'], grouped_df['PageViews/Orders Ratio'], label='PageViews/Orders Ratio')
    ax1.set_xlabel('Product name')
    ax1.set_ylabel('PageViews/Orders Ratio')
    ax1.tick_params(axis='y')
    plt.xticks(rotation=45, ha='right')

    # Create a secondary y-axis for 'PageViews/Orders Ratio'
    ax2 = ax1.twinx()
    ax2.plot(grouped_df['Product name'], grouped_df['Page views'], linestyle='--', marker='x', color='tab:orange', label='Page views')
    ax2.set_ylabel('Page views')
    ax2.tick_params(axis='y')

    # Customize the chart
    plt.title('Page Views and PageViews/Orders Ratio for Products')

    # Set the y-axis limits to start from 0
    ax1.set_ylim(bottom=0)
    ax2.set_ylim(bottom=0)

    ax1.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # Display the chart in your Streamlit app
    st.pyplot(plt)

    mean = grouped_df['PageViews/Orders Ratio'].mean()
    rounded_mean = round(mean, 2)
    median = grouped_df['PageViews/Orders Ratio'].median()
    rounded_median = round(median, 2)
    st.markdown("<p class='body-text'>Mean: " + str(rounded_mean) + "</p>", unsafe_allow_html=True)
    st.markdown("<p class='body-text'>Median: " + str(rounded_median) + "</p>", unsafe_allow_html=True)

    st.markdown("<p class='body-text'>In this chart we can take a deeper look into each type and see how is every product performing. For example, for type 'Crossbody Bags' product  Harbor and Miller perform really well, meaning they need very few page views to generate an order.</p>", unsafe_allow_html=True)
    st.markdown("<p style='font-weight: bold;' class='body-text'>Opportunity</p>", unsafe_allow_html=True)
    st.markdown("<p class='body-text'>'Callie' is one of the products with most views, but it is the worst performer. It needs approximately 16 page views to generate an order while the median of the category is 8. Something you could test is updating the images displayed on the product and see if the conversion improves.</p>", unsafe_allow_html=True)



def generate_page_views_and_ratio_by_category_with_selector(data_original):
    st.markdown("<h1 class='title-text'>Page Views and Page Views / Orders Evolution by Product Type</h1>", unsafe_allow_html=True)

    data = data_original.copy()

    # Create a selectbox for type selection with default value
    selected_type = st.selectbox(
        "Select Product Type",
        data['Type'].unique(),
        key="generate_page_views_and_ratio_by_category_with_selector"
    )

    # Filter the data based on selected types
    filtered_data = data[data['Type'] == selected_type]

    # Create a line chart using matplotlib
    fig, ax1 = plt.subplots(figsize=(10, 6))

    for product_type, group in filtered_data.groupby('Type'):
        group = group.groupby('Date').agg({'Page views': 'sum', 'Orders': 'sum'})
        group['Page views / Orders'] = group.apply(lambda row: row['Page views'] / row['Orders'] if row['Orders'] > 0 else 0, axis=1)
        group.index = pd.to_datetime(group.index)  # Convert 'Date' column to datetime index
        ax1.plot(group.index, group['Page views'], label=f'{product_type} Page Views', marker='o')
        
        # Add a secondary y-axis for Page views / Orders
        ax2 = ax1.twinx()
        ax2.plot(group.index, group['Page views / Orders'], label=f'{product_type} Page Views / Orders', linestyle='--', marker='x', color='tab:orange')

    ax1.set_xlabel('Date')
    ax1.set_ylabel('Page Views', color='tab:blue')
    ax1.legend(loc='upper left')
    
    ax2.set_ylabel('Page Views / Orders', color='tab:orange')
    ax2.legend(loc='upper right')

    # Set the y-axis limits to start from 0
    ax1.set_ylim(bottom=0)
    ax2.set_ylim(bottom=0)
    
    # Display the plot using Streamlit
    st.pyplot(fig)

def generate_page_views_and_ratio_by_product_with_selector(data_original):
    st.markdown("<h1 class='title-text'>Page Views and Page Views / Orders Evolution by Product</h1>", unsafe_allow_html=True)
    data = data_original.copy()
    # Find the default selected products with the most views in 2023
    most_viewed_product = data.groupby('Product name')['Page views'].sum().idxmax()

    options = data['Product name'].unique()
    default_index = options.tolist().index(most_viewed_product)

    # Create a selectbox for type selection with default value
    selected_product = st.selectbox(
        "Select Product",
        options,
        key="generate_page_views_and_ratio_by_product_with_selector",
        index=default_index
    )

    # Filter data for selected products
    filtered_data = data[data['Product name'] == selected_product]

    monthly_data = filtered_data.resample('M', on='Date').agg({'Page views': 'sum', 'Orders': 'sum'})
    monthly_data['Page views / Orders ratio'] = monthly_data.apply(lambda row: row['Page views'] / row['Orders'] if row['Orders'] > 0 else 0, axis=1)
    # Add a 'Date' column to the DataFrame
    monthly_data['Date'] = monthly_data.index
    # we change date to format YYYY/MM
    monthly_data['Date'] = monthly_data['Date'].dt.strftime("%Y-%m")

    # Create the Matplotlib chart
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot 'Page views' on the primary y-axis
    ax1.plot( monthly_data['Date'].astype(str), monthly_data['Page views'], marker='o', label='Page Views')
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Page views')
    #ax1.tick_params(axis='y')
    plt.xticks(rotation=45, ha='right')

    # Create a secondary y-axis for 'PageViews/Orders Ratio'
    ax2 = ax1.twinx()
    ax2.plot(monthly_data['Date'].astype(str), monthly_data['Page views / Orders ratio'], linestyle='--', marker='x', color='tab:orange', label='Page Views/Orders Ratio')
    ax2.set_ylabel('Page Views/Orders Ratio')
    #ax2.tick_params(axis='y')

    # Set the y-axis limits to start from 0
    ax1.set_ylim(bottom=0)
    ax2.set_ylim(bottom=0)

    plt.legend()
    st.pyplot(plt)