import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def reviews_by_month(df_reviews):

    df_reviews = df_reviews.copy()
    # Convert 'created_at' to datetime
    df_reviews['created_at'] = pd.to_datetime(df_reviews['created_at'], unit='ms')

    # Get the date 12 months ago from the most recent date
    most_recent_date = df_reviews['created_at'].max()
    twelve_months_ago = most_recent_date - timedelta(days=365)

    # Filter the data for the last 12 months
    df_filtered = df_reviews[df_reviews['created_at'] >= twelve_months_ago]

    # Group by month and count the reviews
    monthly_reviews = df_filtered.groupby(df_filtered['created_at'].dt.to_period("M")).size().reset_index(name='count')
    monthly_reviews['created_at'] = monthly_reviews['created_at'].dt.to_timestamp()

    # Sort the data by date
    monthly_reviews = monthly_reviews.sort_values('created_at')

    # Create the bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(monthly_reviews['created_at'], monthly_reviews['count'], width=20)
    ax.set_title('Number of Reviews per Month (Last 12 Months)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of Reviews')

    # Format x-axis to show month names
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
    fig.autofmt_xdate()  # Rotate and align the tick labels

    # Display the chart in Streamlit
    st.pyplot(fig)

def get_retailers_with_reviews_purchase_last_60_days(df_orders, df_reviews, data_last_update):
    df_orders = df_orders.copy()

    # Convert date columns to datetime if not already
    df_reviews['created_at'] = pd.to_datetime(df_reviews['created_at'], unit='ms')
    df_orders['brand_contacted_at_values'] = pd.to_datetime(df_orders['brand_contacted_at_values'], unit='ms')

    # 1. Filter orders data for last 60 days
    today = pd.to_datetime(data_last_update)
    cutoff_date = today - pd.DateOffset(days=60)
    df_orders_filtered = df_orders[df_orders['brand_contacted_at_values'] >= cutoff_date]

    # 2. Identify retailers who have left reviews
    merged_df = pd.merge(df_orders_filtered, df_reviews, left_on='retailer_names', right_on='retailer_name', how='left')

    # Count reviews left by each retailer
    retailer_review_counts = merged_df.groupby('retailer_name')['rating'].count().reset_index()
    retailer_review_counts.rename(columns={'rating': 'review_count'}, inplace=True)

    # 3. Remove retailers who left a review for their last order
    last_order_retailers = df_orders_filtered.loc[df_orders_filtered.groupby('retailer_names')['brand_contacted_at_values'].idxmax()]
    retailers_left_review_last_order = pd.merge(last_order_retailers, df_reviews, left_on='tokens', right_on='brand_order_token', how='inner')['retailer_names'].to_list()

    final_retailers = retailer_review_counts[~retailer_review_counts['retailer_name'].isin(retailers_left_review_last_order)]

    # Order by review count descending
    final_retailers = final_retailers.sort_values(by='review_count', ascending=False)

    # Join with df_orders to get retailer_tokens
    final_retailers = pd.merge(final_retailers, df_orders[['retailer_names', 'retailer_tokens', 'brand_contacted_at_values']], 
                               left_on='retailer_name', right_on='retailer_names', how='left')

    # Drop duplicate rows and unnecessary columns
    final_retailers = final_retailers.drop_duplicates(subset='retailer_name').drop(columns=['retailer_names'])

    # Calculate days since order
    final_retailers['days_since_order'] = (today - final_retailers['brand_contacted_at_values']).dt.days

    # Get the date of the last order
    final_retailers['last_order_date'] = final_retailers['brand_contacted_at_values'].dt.date

    # Format retailer_tokens as a link
    final_retailers['retailer_tokens'] = final_retailers['retailer_tokens'].apply(
        lambda x: f'<a href="https://www.faire.com/brand-portal/messages/{x}" target="_blank">Send a DM</a>'
    )

    # Reset index and select final columns
    final_retailers = final_retailers[['retailer_name', 'review_count', 'retailer_tokens', 'days_since_order', 'last_order_date']].reset_index(drop=True)

    final_retailers.columns = ['Retailer Name', 'Review Count', 'Send a DM', 'Days Since Last Order', 'Last Order Date']

    # we push Send a DM column to the last position
    cols = final_retailers.columns.tolist()
    cols = cols[:2] + cols[3:] + [cols[2]]
    final_retailers = final_retailers[cols]

    # Convert DataFrame to HTML table
    html_table = final_retailers.to_html(classes='display', index=False, table_id='myTable', escape=False)

    # HTML template with DataTables integration
    html = f"""  
    <!DOCTYPE html>
    <html>
    <head>
        <link href="https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.10.21/css/jquery.dataTables.css">
        <script type="text/javascript" charset="utf8" src="https://code.jquery.com/jquery-3.5.1.js"></script>
        <script type="text/javascript" charset="utf8" src="https://cdn.datatables.net/1.10.21/js/jquery.dataTables.js"></script>
        <style>
            body {{
                font-family: 'Source Sans Pro', sans-serif;
            }}
            #myTable {{
                width: 100%;
                border-collapse: collapse;
                margin-bottom: 20px;
            }}
            #myTable th, #myTable td {{
                padding: 12px;
                border: 1px solid #ddd;
            }}
            #myTable th {{
                background-color: #f2f2f2;
                font-weight: 600;
                text-align: left;
            }}
            #myTable tr:nth-child(even) {{
                background-color: #f8f8f8;
            }}
            #myTable tr:hover {{
                background-color: #e8e8e8;
            }}
            .dataTables_wrapper .dataTables_length, 
            .dataTables_wrapper .dataTables_filter, 
            .dataTables_wrapper .dataTables_info, 
            .dataTables_wrapper .dataTables_processing, 
            .dataTables_wrapper .dataTables_paginate {{
                margin-bottom: 10px;
                font-family: 'Source Sans Pro', sans-serif;
            }}
        </style>
        <script>
            $(document).ready(function() {{
                $('#myTable').DataTable({{
                    "pageLength": 25,
                    "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]]
                }});
            }});
        </script>
    </head>
    <body>
        {html_table}
    </body>
    </html>
    """

    # Display the HTML using st.components.v1.html
    st.components.v1.html(html, height=600, scrolling=True)