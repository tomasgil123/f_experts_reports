import pandas as pd
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def get_evolution_rankings_products_given_query(df, query):

    df = df.copy()
    # Convert execution_date to datetime
    df['execution_date'] = pd.to_datetime(df['execution_date'])

    # Filter by query
    filtered_df = df[df['search_query'] == query]

    # if there is no data for the query we display a message
    if filtered_df.empty:
        st.markdown(f"""
                    ##### No products rank within the top 100 for the search query: '{query}'.
                    """)
        return

    # sort by execution_date in ascending order
    filtered_df = filtered_df.sort_values(by='execution_date')

    # Pivot the dataframe to have dates as index and titles as columns
    pivot_df = filtered_df.pivot(index='execution_date', columns='title', values='order')

   # Plotting the chart
    fig, ax = plt.subplots()
    for column in pivot_df:
        ax.plot(pivot_df.index, pivot_df[column], marker='o', label=column)

    ax.set_xlabel('Execution Date')
    ax.set_ylabel('Order')
    ax.set_title(f'Ranking Evolution for Query: {query}')
    ax.legend(title='Product Title', bbox_to_anchor=(1.05, 1), loc='upper left')
    ax.invert_yaxis()  # Invert y-axis to show top rankings at the top
    ax.set_ylim(0, 100)  # Set y-axis limits from 0 to 100

    # Set the number of x-ticks
    ax.set_xticks(pivot_df.index)
    ax.set_xticklabels(pivot_df.index.strftime('%Y-%m-%d'), rotation=45)

    ax.grid(True)

    plt.xticks(rotation=45)

    st.pyplot(fig)


def get_brands_with_most_products_in_top_100(df, brand, query):

    df = df.copy()
    # Convert execution_date to datetime
    df['execution_date'] = pd.to_datetime(df['execution_date'])

    # Filter by max date
    max_date = df['execution_date'].max()
    filtered_df = df[(df['execution_date'] == max_date) & (df['query'] == query)]

    # Get the top 5 brands with most products in the top 100
    top_brands = filtered_df.nlargest(5, 'count')

    # Check if the specific brand is in the top 9
    if brand not in top_brands['product_count'].values:
        # Get the specific brand data
        selected_brand_data = df[df['product_count'] == brand]

        if selected_brand_data.empty:
            selected_brand_data = pd.DataFrame({
                'execution_date': [df['execution_date'].max()],
                'product_count': [brand],
                'count': [0],
                'query': [query]
            })

        # if we cant find data for the selected brand, we 

        # Append the specific brand data to the top brands dataframe
        top_brands = pd.concat([top_brands, selected_brand_data])

    # Ensure the top 9 brands are in descending order
    top_brands = top_brands.sort_values(by='count', ascending=False)

    st.markdown(f"""
                #### Top 5 brands with the most products in search results for '{query}'
                """)

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(top_brands['product_count'], top_brands['count'], color=['blue' if brand != brand else 'skyblue' for brand in top_brands['product_count']])
    ax.set_xlabel('Brands')
    ax.set_ylabel('Number of Products')
    plt.xticks(rotation=45)

    # Display the chart and the count in Streamlit
    st.pyplot(fig)
