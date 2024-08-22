import pandas as pd

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

    return final_retailers