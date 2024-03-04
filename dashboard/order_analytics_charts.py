import streamlit as st
import pandas as pd
import matplotlib.ticker as mtick
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def lifetime_performance_metrics(df, day_data_was_obtained):
    df = df.copy()

    # Calculate the date range for the last 12 months and last 3 months
    current_date = day_data_was_obtained
    last_12_months_start = current_date - timedelta(days=365)
    last_3_months_start = current_date - timedelta(days=90)

    # Filter data for the last 12 months
    last_12_months_data = df[df['brand_contacted_at_values'] >= last_12_months_start]

    # Filter data for the last 3 months
    last_3_months_data = df[df['brand_contacted_at_values'] >= last_3_months_start]

    # Calculate GMV (gross merchandise value)
    gmv_last_12_months = last_12_months_data['payout_total_values'].sum()
    gmv_last_3_months = last_3_months_data['payout_total_values'].sum()

    # Calculate average order value
    average_order_value_last_12_months = last_12_months_data['payout_total_values'].mean()
    average_order_value_last_3_months = last_3_months_data['payout_total_values'].mean()

    # Calculate number of orders
    num_orders_last_12_months = last_12_months_data.shape[0]
    num_orders_last_3_months = last_3_months_data.shape[0]
    
    card_data = [
        {"title": "Total Sales", "value": f"${gmv_last_12_months:,.2f}"},
        {"title": "Average Order Value", "value": f"${average_order_value_last_12_months:,.2f}"},
        {"title": "Number of Orders", "value": f"{num_orders_last_12_months:,}"},
        {"title": "Total Sales", "value": f"${gmv_last_3_months:,.2f}"},
        {"title": "Average Order Value", "value": f"${average_order_value_last_3_months:,.2f}"},
        {"title": "Number of Orders", "value": f"{num_orders_last_3_months:,}"}
    ]
    # First Row
    st.markdown(f"""
                #### Last 12 months:
    <div class="row">
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[0]["title"]}</h5>
            <p class="card-text">Value: {card_data[0]["value"]}</p>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[1]["title"]}</h5>
            <p class="card-text">Value: {card_data[1]["value"]}</p>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[2]["title"]}</h5>
            <p class="card-text">Value: {card_data[2]["value"]}</p>
            </div>
        </div>
        </div>
    </div>

    #### Last 90 days:

    <div class="row">
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[3]["title"]}</h5>
            <p class="card-text">Value: {card_data[3]["value"]}</p>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[4]["title"]}</h5>
            <p class="card-text">Value: {card_data[4]["value"]}</p>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[5]["title"]}</h5>
            <p class="card-text">Value: {card_data[5]["value"]}</p>
            </div>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def sales_per_quarter(df):
    df = df.copy()

    # Extract quarter and year from brand_contacted_at_values
    df['quarter_year'] = df['brand_contacted_at_values'].dt.to_period('Q')

    # Group by quarter and sum the sales
    sales_per_quarter = df.groupby('quarter_year')['payout_total_values'].sum()

   # Plotting
    fig, ax = plt.subplots()
    sales_per_quarter.plot(kind='line', marker='o', ax=ax)
    ax.set_xlabel('Quarter')
    ax.set_ylabel('Sales')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, None)
    plt.tight_layout()

    plt.title('Sales per Quarter', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display in Streamlit
    st.pyplot(fig)

def get_previous_months(current_month):
    # List to store previous months
    previous_months = [current_month.strftime('%Y/%m')]
    
    # Calculate 11 previous months
    for i in range(1, 12):
        previous_month = current_month - i
        previous_months.append(previous_month.strftime('%Y/%m'))
    
    return previous_months

def sales_previous_year_vs_sales_year_before_that_one(df, day_data_was_obtained):
    df = df.copy()

    # Group orders by month and calculate total sales
    df['month'] = pd.to_datetime(df['brand_contacted_at_values']).dt.to_period('M')
    sales_by_month = df.groupby('month')['payout_total_values'].sum()

    # Get the last 12 months and 12 months prior to those months
    current_month = pd.Period(day_data_was_obtained, 'M')
    last_12_months = get_previous_months(current_month)[::-1]
    current_month_12_months_ago = current_month - 12
    previous_12_months = get_previous_months(current_month_12_months_ago)[::-1]

    sales_last_12_months = sales_by_month[last_12_months]
    sales_last_12_months = sales_last_12_months.to_frame().reset_index()
    sales_last_12_months['month_name'] = sales_last_12_months['month'].dt.strftime('%B')

    # drop the month column
    sales_last_12_months = sales_last_12_months.drop(columns=['month'])

    sales_previous_12_months = sales_by_month[previous_12_months]
    sales_previous_12_months = sales_previous_12_months.to_frame().reset_index()
    sales_previous_12_months['month_name'] = sales_previous_12_months['month'].dt.strftime('%B')
    # drop the month column
    sales_previous_12_months = sales_previous_12_months.drop(columns=['month'])

    # we merge both dataframe by column "month_name"
    sales_versus = sales_last_12_months.merge(sales_previous_12_months, on="month_name", suffixes=('_last_12_months', '_previous_12_months'))

    # Plot
    fig, ax = plt.subplots()
    ax.plot(sales_versus["month_name"], sales_versus["payout_total_values_last_12_months"], marker='o', label='12 month lookback')
    ax.plot(sales_versus["month_name"], sales_versus["payout_total_values_previous_12_months"], marker='o', label='13-24 month lookback')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, None)
    plt.tight_layout()

    # Streamlit app
    plt.title('Sales performance month over month', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    st.pyplot(fig)

def orders_previous_year_vs_orders_year_before_that_one(df, day_data_was_obtained):
    df = df.copy()

    # Group orders by month and calculate total sales
    df['month'] = pd.to_datetime(df['brand_contacted_at_values']).dt.to_period('M')
    # Group by month and count the number of orders
    orders_by_month = df.groupby('month').size()

    # Get the last 12 months and 12 months prior to those months
    current_month = pd.Period(day_data_was_obtained, 'M')
    last_12_months = get_previous_months(current_month)[::-1]
    current_month_12_months_ago = current_month - 12
    previous_12_months = get_previous_months(current_month_12_months_ago)[::-1]

    sales_last_12_months = orders_by_month[last_12_months]
    sales_last_12_months = sales_last_12_months.to_frame().reset_index()
    sales_last_12_months['month_name'] = sales_last_12_months['month'].dt.strftime('%B')

    # drop the month column
    sales_last_12_months = sales_last_12_months.drop(columns=['month'])

    sales_previous_12_months = orders_by_month[previous_12_months]
    sales_previous_12_months = sales_previous_12_months.to_frame().reset_index()
    sales_previous_12_months['month_name'] = sales_previous_12_months['month'].dt.strftime('%B')
    # drop the month column
    sales_previous_12_months = sales_previous_12_months.drop(columns=['month'])

    # we merge both dataframe by column "month_name"
    sales_versus = sales_last_12_months.merge(sales_previous_12_months, on="month_name", suffixes=('_last_12_months', '_previous_12_months'))

    # Plot
    fig, ax = plt.subplots()
    ax.plot(sales_versus["month_name"], sales_versus["0_last_12_months"], marker='o', label='12 month lookback')
    ax.plot(sales_versus["month_name"], sales_versus["0_previous_12_months"], marker='o', label='13-24 month lookback')
    ax.set_xlabel('Month')
    ax.set_ylabel('Sales')
    ax.tick_params(axis='x', rotation=45)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    ax.set_ylim(0, None)
    plt.tight_layout()

    # Streamlit app
    plt.title('Number of orders performance month over month', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    st.pyplot(fig)

def sales_by_source(df, day_data_was_obtained):
    df = df.copy()

    # Extract month from timestamp
    df['month'] = df['brand_contacted_at_values'].dt.to_period('M')

    # Filter data for the last 12 months
    last_12_months = day_data_was_obtained - timedelta(days=365)
    df_last_12_months = df[df['brand_contacted_at_values'] >= last_12_months]

    # Aggregate sales data by source
    sales_by_source = df_last_12_months.groupby(['month', 'sources'])['payout_total_values'].sum().unstack()
    
    # Normalize data to represent 100% of sales
    sales_by_source_percentage = sales_by_source.div(sales_by_source.sum(axis=1), axis=0) * 100

    # Create figure and axis objects
    fig, ax = plt.subplots()

    # Plot stacked bar chart
    sales_by_source_percentage.plot(kind='bar', stacked=True, ax=ax)
    ax.set_xlabel('Source')
    ax.set_ylabel('Total Sales (%)')
    ax.set_xticklabels(sales_by_source_percentage.index.strftime('%b %Y'), rotation=45)
    ax.legend()
    plt.tight_layout()

    # Custom legend with desired names
    legend_labels = ['Faire Direct', 'Marketplace', 'Source 3', 'Source 4', 'Source 5']
    plt.legend(legend_labels)

    plt.title('Faire Direct sales vs Marketplace sales month over month', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Add % symbol to y-axis tick labels
    fmt = '%.0f%%'  # Format as percentage with no decimal places
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: fmt % x))

    # Display chart in Streamlit
    st.pyplot(fig)

def new_merchants_by_source(df, day_data_was_obtained):

    # Filter rows where either 'first_order_for_brand_values' or 'very_first_order_for_brand_values' is True
    new_merchants_df = df[(df['first_order_for_brand_values'] == True) | (df['very_first_order_for_brand_values'] == True)]

    # Group by month and count the number of new merchants for each month in the last 12 months
    current_date = day_data_was_obtained
    last_12_months = current_date - pd.DateOffset(months=12)
    new_merchants_by_month_and_source = new_merchants_df[new_merchants_df['brand_contacted_at_values'] >= last_12_months] \
                                .groupby([pd.Grouper(key='brand_contacted_at_values', freq='M'), 'sources']) \
                                .size()
    # Pivot the data for plotting
    pivot_data = new_merchants_by_month_and_source.unstack(fill_value=0)

    # Create figure and axes
    fig, ax = plt.subplots()

    # Set the width of the bars
    bar_width = 0.35

    # Generate positions for bars
    bar_positions = range(len(pivot_data))

    # Plot bars for each source
    for i, (source, data) in enumerate(pivot_data.items()):
        ax.bar([pos + i * bar_width for pos in bar_positions], data, bar_width, label=source)

    # Set labels and title
    ax.set_xlabel('Month')
    ax.set_ylabel('Number of New Merchants')
    ax.set_xticks(bar_positions)
    ax.set_xticklabels(pivot_data.index.strftime('%Y-%m'), rotation=45)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    # Custom legend with desired names
    legend_labels = ['Faire Direct', 'Marketplace', 'Source 3', 'Source 4', 'Source 5']
    plt.legend(legend_labels)

    # Show plot
    plt.tight_layout()

    plt.title('New Merchants by Month and Source', fontsize=13, loc='left', pad=12, fontweight=500, color="#31333f", fontfamily="Microsoft Sans Serif")

    # Display chart in Streamlit
    st.pyplot(fig)

def cumulative_distribution_of_retailers(df, day_data_was_obtained):
    # we make a copy of the dataframe 
    df = df.copy()
    # Calculate the date 12 months ago from today
    last_12_months_date = day_data_was_obtained - timedelta(days=365)

        # Filter the DataFrame for the last 12 months
    df_last_12_months = df[df['brand_contacted_at_values'] >= last_12_months_date]

    # Group by retailer_tokens and sum the payout_total_values for each retailer
    sales_by_retailer = df_last_12_months.groupby('retailer_tokens')['payout_total_values'].sum().sort_values(ascending=False)

    # Calculate the total sales across all retailers
    total_sales = sales_by_retailer.sum()

    # Calculate the percentage of total sales for each retailer
    sales_percentage = (sales_by_retailer / total_sales) * 100

    # Calculate the cumulative distribution of sales percentage
    sales_cdf = sales_percentage.cumsum()

    # Create an array representing the percentage of retailers
    num_retailers = len(sales_cdf)
    retailers_percentage = [i / num_retailers * 100 for i in range(1, num_retailers + 1)]


    # Creating the figure and axes
    fig, ax = plt.subplots()

    # Plotting
    ax.plot(retailers_percentage, sales_cdf, marker='o', linestyle='-')
    ax.set_title('CDF of Sales Percentage vs Retailers Percentage', loc='left')
    ax.set_xlabel('Percentage of Retailers')
    ax.set_ylabel('Percentage of Sales')
    ax.grid(True)

    # Adjusting x-axis ticks
    ax.set_xticks(range(0, 101, 10))
    plt.tight_layout()

    # Display chart in Streamlit
    st.pyplot(fig)

def sales_by_retailer(df, day_data_was_obtained):
    # we make a copy of the dataframe 
    df = df.copy()

    # Calculate the date 12 months ago from today
    last_12_months_date = day_data_was_obtained - timedelta(days=365)

    # Filter the DataFrame for the last 12 months
    df_last_12_months = df[df['brand_contacted_at_values'] >= last_12_months_date]

    # Group by retailer_tokens and sum the payout_total_values for each retailer
    sales_by_retailer = df_last_12_months.groupby('retailer_tokens')['payout_total_values'].sum().sort_values(ascending=False)

    # Calculate the total sales across all retailers
    total_sales = sales_by_retailer.sum()

    # Calculate the percentage of total sales for each retailer
    sales_percentage = (sales_by_retailer / total_sales) * 100

    # Get the top 5% of retailers
    top_retailers = sales_percentage[sales_percentage >= sales_percentage.quantile(0.95)]

    # Creating the figure and axes
    fig, ax = plt.subplots()

    # Plotting
    top_retailers.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Percentage of Total Sales by Top 5% Retailers (Last 12 Months)')
    ax.set_xlabel('Retailer')
    ax.set_ylabel('Percentage of Total Sales')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-labels for better readability

    # Add % symbol to y-axis tick labels
    fmt = '%.0f%%'  # Format as percentage with no decimal places
    plt.gca().yaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: fmt % x))

    plt.tight_layout()

    st.pyplot(fig)

