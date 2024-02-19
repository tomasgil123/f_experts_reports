import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import re
from collections import Counter
from wordcloud import WordCloud
from datetime import datetime, timedelta

def get_competitors_total_reviews(data):
    brand_reviews = data.groupby('brand')['ratings'].count()
    brand_reviews = brand_reviews.sort_values(ascending=False)
    fig, ax = plt.subplots()

    # Set the title and labels for the chart displaying the number of reviews
    ax.set_xlabel('Brand')
    ax.set_ylabel('Number of Reviews')

    # Plot the number of reviews as a bar chart
    brand_reviews.plot(kind='bar', ax=ax)

    # Customize the appearance of the chart if needed
    plt.xticks(rotation=45)  # Rotate the x-axis labels for better readability

    plt.title('Total Reviews per Brand', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display the chart in your Streamlit app
    st.pyplot(fig)

def get_competitors_average_rating(data):
     average_rating = data.groupby('brand')['ratings'].mean()
     average_rating = average_rating.round(1)
    
    # Create a figure and axis for the table
     fig, ax = plt.subplots(figsize=(6, 2))  # Adjust the figsize as needed
    
    # Create a table from the DataFrame and add it to the axis
     table = ax.table(cellText=average_rating.reset_index().values,
                     colLabels=['Brand', 'Average Rating'],
                     cellLoc='center',
                     loc='center',
                     colColours=['lightgray']*2)  # Customize the table appearance
    
    # Hide axis
     ax.axis('off')
    
     plt.title("Average rating per brand", fontsize=12, loc='left', pad=0, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")
     st.pyplot(fig)

def get_competitors_reviews_by_month(df):
    # Convert timestamps to datetime
    df['publish_at_values'] = pd.to_datetime(df['publish_at_values'], unit='ms')
    df['created_at_values'] = pd.to_datetime(df['created_at_values'], unit='ms')

    # Define the date range for the last 12 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    # Filter data for the last 12 months
    df = df[(df['publish_at_values'] >= start_date) & (df['publish_at_values'] <= end_date)]

    # Sidebar: Brand selector
    selected_brand = st.selectbox("Select Brand", df['brand'].unique())

    # Filter data based on selected brand
    filtered_df = df[df['brand'] == selected_brand]

    # Group data by month and count the number of reviews
    monthly_reviews = filtered_df.resample('M', on='publish_at_values').size()

    # Create a bar chart
    plt.figure()
    plt.bar(monthly_reviews.index.strftime('%b %Y'), monthly_reviews)
    plt.xlabel('Month')
    plt.ylabel('Number of Reviews')
    plt.xticks(rotation=45)

    plt.title("Reviews per month (last 12 months)", fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    st.pyplot(plt)

def get_competitors_most_common_words_in_reviews(data):
    selected_brand = st.selectbox('Select a Brand:', data['brand'].unique())
    reviews = data[data['brand'] == selected_brand]['titles'].str.cat(sep=' ')
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(reviews)
    plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')

    plt.title(f'Most Common Words in Reviews for {selected_brand}', fontsize=13, loc='left', pad=20, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display the word cloud
    col1, col2, col3 = st.columns([0.05,0.9,0.05])

    with col2:
        st.pyplot(plt)
    

def get_competitors_most_common_words_title(df):
    # Create a brand selector widget
    selected_brand = st.selectbox("Select a Brand", df['brand'].unique())
    # Create a product category selector widget
    selected_category = st.selectbox("Select a Product Category", df['Product Category'].unique())

    # Filter the data based on the selected brand and category
    filtered_df = df[(df['brand'] == selected_brand) & (df['Product Category'] == selected_category)]

    # Tokenize and count words in product names
    product_names = filtered_df['Product Name'].str.lower()
    words = re.findall(r'\b\w+\b', ' '.join(product_names))
    word_counts = Counter(words)

    # Convert word counts to a DataFrame for plotting
    word_counts_df = pd.DataFrame.from_dict(word_counts, orient='index', columns=['Count']).reset_index()
    word_counts_df = word_counts_df.rename(columns={'index': 'Word'})

    # Sort the DataFrame by word count in descending order
    word_counts_df = word_counts_df.sort_values(by='Count', ascending=False)

    # Create a bar chart with Matplotlib
    plt.figure()
    plt.bar(word_counts_df['Word'].head(15), word_counts_df['Count'].head(15))
    plt.xlabel('Word')
    plt.ylabel('Count')
    plt.xticks(rotation=45)

    plt.title(f'Most Common Words in Product Titles for {selected_brand} in {selected_category}', fontsize=12, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")
    
    # Display the bar chart using Streamlit
    st.pyplot(plt)

    # Create a word cloud for visualization
    wordcloud = WordCloud(width=600, height=300, background_color='white').generate_from_frequencies(word_counts)

    # Display the word cloud
    col1, col2, col3 = st.columns([0.05,0.9,0.05])

    with col2:
        st.image(wordcloud.to_array())


def get_competitors_price_distribution_by_category(df):
    all_brands_option = "All Brands"
    selected_brand = st.selectbox("Select Brand", np.append(df['brand'].unique(), all_brands_option))
    selected_category = st.selectbox("Select Category", df['Product Category'].unique(), index=0)

        # Filter data based on user selections
    if selected_brand == all_brands_option:
        filtered_df = df[df['Product Category'] == selected_category]
    else:
        filtered_df = df[(df['brand'] == selected_brand) & (df['Product Category'] == selected_category)]

    # Create a histogram for the distribution of retail prices using Matplotlib
    plt.figure()
    plt.hist(filtered_df['Wholesale Price'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Wholesale Price')
    plt.ylabel('Frequency')
    plt.title(f'Price Distribution for {selected_category} by {selected_brand}', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")
    plt.xlim(left=0)  # Set the x-axis limit to start from 0
    st.pyplot(plt)

def get_competitors_minimum_order_data(data):
    data = data.copy()
    # sort in asceding order by first order minimum amount
    data = data.sort_values(by='First Order Minimum Amount', ascending=True)
    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()

    # Set x-axis labels to be the Brand Names
    brand_names = data['Brand Name']
    x = range(len(brand_names))

    # Plot First Order Minimum Amount
    first_order_min = data['First Order Minimum Amount']
    ax.bar(x, first_order_min, width=0.25, label='First Order Minimum Amount', align='center')

    # Plot Reorder Minimum Amount
    reorder_min = data['Reorder Minimum Amount']
    ax.bar(x, reorder_min, width=0.25, label='Reorder Minimum Amount', align='edge')

    # Set x-axis labels and legend
    ax.set_xticks(x)
    ax.set_xticklabels(brand_names, rotation=45, ha='right')
    ax.legend()

    # Set labels and title
    ax.set_xlabel('Brand Name')
    ax.set_ylabel('Amount')

    plt.title('First Order and Reorder Minimum Amount per Brand', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    st.pyplot(fig)

def get_competitors_fulfillment_data(data):
    # make a copy of the data
    data = data.copy()
    data.sort_values(by='Upper Bound Lead Time Days', ascending=True, inplace=True)
    # Create a bar chart using Matplotlib
    fig, ax = plt.subplots()

    # Set x-axis labels to be the Brand Names
    brand_names = data['Brand Name']
    x = range(len(brand_names))

    # Plot Upper Bound Lead Time Days
    upper_lead_time = data['Upper Bound Lead Time Days']
    ax.bar(x, upper_lead_time, width=0.4, label='Upper Bound Lead Time Days', align='center')

    # Plot Lower Bound Lead Time Days
    lower_lead_time = data['Lower Bound Lead Time Days']
    ax.bar(x, lower_lead_time, width=0.4, label='Lower Bound Lead Time Days', align='edge')

    # Set x-axis labels and legend
    ax.set_xticks(x)
    ax.set_xticklabels(brand_names, rotation=45, ha='right')
    ax.legend()

    # Set labels and title
    ax.set_xlabel('Brand Name')
    ax.set_ylabel('Lead Time Days')

    plt.title('Fulfillment speed per Brand', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display the chart using Streamlit
    st.pyplot(fig)

def get_number_collections_per_brand(df):
    # Group by brand and count the number of collections
    brand_counts = df['brand'].value_counts()
    # Plotting
    fig, ax = plt.subplots()
    brand_counts.plot(kind='bar', ax=ax)
    ax.set_xlabel('Brand')
    ax.set_ylabel('Number of Collections')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()

    plt.title('Number of collections per Brand', fontsize=14, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display the plot using Streamlit
    st.pyplot(fig)

def get_median_maturity_collections_per_brand(df):
    # Convert created_at to datetime format
    df['created_at'] = pd.to_datetime(df['created_at'], unit='ms')

    # Calculate time differences
    current_date = datetime.now()
    df['time_since_creation'] = (current_date - df['created_at']).dt.days

    # Group by brand and calculate the mean time since creation
    brand_time_since_creation = df.groupby('brand')['time_since_creation'].median().sort_values()

    # Plotting
    fig, ax = plt.subplots()
    brand_time_since_creation.plot(kind='bar', ax=ax)
    ax.set_xlabel('Brand')
    ax.set_ylabel('Median Time Since Creation (days)')
    ax.set_xticklabels(brand_time_since_creation.index, rotation=45, ha='right')
    plt.tight_layout()

    plt.title('Median Time Since Creation of Collections by Brand', fontsize=14, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display the plot using Streamlit
    st.pyplot(fig)
def get_median_update_time_collections_per_brand(df):
    # Convert updated_at to datetime format
    df['updated_at'] = pd.to_datetime(df['updated_at'], unit='ms')

    # Calculate time differences
    current_date = datetime.now()
    df['time_since_update'] = (current_date - df['updated_at']).dt.days

    # Group by brand and calculate the mean time since update
    brand_time_since_update = df.groupby('brand')['time_since_update'].median().sort_values()

    # Plotting
    fig, ax = plt.subplots()
    brand_time_since_update.plot(kind='bar', ax=ax)
    ax.set_xlabel('Brand')
    ax.set_ylabel('Median Time Since Last Update (days)')
    ax.set_xticklabels(brand_time_since_update.index, rotation=45, ha='right')
    plt.tight_layout()

    plt.title('Median Time Since Last Update of Collections by Brand', fontsize=14, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")


    # Display the plot using Streamlit
    st.pyplot(fig)

def get_median_items_per_collection_per_brand(df):

    # Group by brand and calculate the median number of total_items
    median_total_items = df.groupby('brand')['total_items'].median().sort_values()

    # Plotting
    fig, ax = plt.subplots()
    median_total_items.plot(kind='bar', ax=ax)
    ax.set_xlabel('Brand')
    ax.set_ylabel('Median Total Items')
    ax.set_xticklabels(median_total_items.index, rotation=45, ha='right')
    plt.tight_layout()

    plt.title('Median Number of Total Items per Collection by Brand', fontsize=14, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")


    # Display the plot using Streamlit
    st.pyplot(fig)