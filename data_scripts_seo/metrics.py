
# Define a function to get the top 100 rows for each date and count the brands
def count_brands_per_date(df):
    top_100_df = df.head(100)
    return top_100_df['brand_name'].value_counts().reset_index().rename(columns={'index': 'brand_name', 'brand_name': 'product_count'})


# Define a function to calculate the median position for each brand for each date
def calculate_median_position(df):
    top_100_df = df.head(100)
    return top_100_df.groupby('brand_name')['order'].median().reset_index().rename(columns={'order': 'median_position'})


def get_brand_product_counts_top_100_per_date(df):
    df = df.copy()

    # Ensure the data is ordered by 'execution_date' and 'order'
    df = df.sort_values(by=['execution_date', 'order'])

    # Group by 'execution_date' and apply the function
    brand_counts_per_date = df.groupby('execution_date').apply(count_brands_per_date).reset_index(level=1, drop=True).reset_index()

    return brand_counts_per_date

def get_brand_median_position_per_date(df):
    df = df.copy()

    # Ensure the data is ordered by 'execution_date' and 'order'
    df = df.sort_values(by=['execution_date', 'order'])

    # Group by 'execution_date' and apply the function
    brand_median_position_per_date = df.groupby('execution_date').apply(calculate_median_position).reset_index(level=1, drop=True).reset_index()

    return brand_median_position_per_date
