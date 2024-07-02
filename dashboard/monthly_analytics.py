
import streamlit as st
from datetime import datetime
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def sales_performance_metrics(df, selected_month, selected_year, selected_month_string):
    # Filter dataframes by selected month and year
    df_current_month = df[(df['brand_contacted_at_values'].dt.month == selected_month) & 
                          (df['brand_contacted_at_values'].dt.year == selected_year)]

    df_previous_month = df[(df['brand_contacted_at_values'].dt.month == selected_month - 1) & 
                           (df['brand_contacted_at_values'].dt.year == selected_year)]

    df_previous_year = df[(df['brand_contacted_at_values'].dt.month == selected_month) & 
                          (df['brand_contacted_at_values'].dt.year == selected_year - 1)]

    # we calculate GMV (gross merchandise value), average order value and total number of orders
    gmv = df_current_month['payout_total_values'].sum()
    average_order_value = df_current_month['payout_total_values'].mean()
    total_orders = df_current_month.shape[0]

    display_previous_month = True
    display_previous_year = True

    # we calculate the percentage of change in GMV, average order value and total orders, if df_previous_month is not empty
    if not df_previous_month.empty:
        gmv_change = ((gmv - df_previous_month['payout_total_values'].sum()) / df_previous_month['payout_total_values'].sum()) * 100
        average_order_value_change = ((average_order_value - df_previous_month['payout_total_values'].mean()) / df_previous_month['payout_total_values'].mean()) * 100
        total_orders_change = ((total_orders - df_previous_month.shape[0]) / df_previous_month.shape[0]) * 100
    else:
        display_previous_month = False
        gmv_change = 0
        average_order_value_change = 0
        total_orders_change = 0
    
    # we calculate the percentage of change in GMV, average order value and total orders, if df_previous_year is not empty
    if not df_previous_year.empty:
        gmv_change_previous_year = ((gmv - df_previous_year['payout_total_values'].sum()) / df_previous_year['payout_total_values'].sum()) * 100
        average_order_value_change_previous_year = ((average_order_value - df_previous_year['payout_total_values'].mean()) / df_previous_year['payout_total_values'].mean()) * 100
        total_orders_change_previous_year = ((total_orders - df_previous_year.shape[0]) / df_previous_year.shape[0]) * 100
    else:
        display_previous_year = False
        gmv_change_previous_year = 0
        average_order_value_change_previous_year = 0
        total_orders_change_previous_year = 0
    
    card_data = [
        {"title": "Total Sales", "value": f"${gmv:,.2f}"},
        {"title": "Average Order Value", "value": f"${average_order_value:,.2f}"},
        {"title": "Total Orders", "value": f"{total_orders:,}"},
        {"title": "Sales Change vs Previous Month", "value": f"{gmv_change:.2f}%", "trend": "up" if gmv_change > 0 else "down"},
        {"title": "Average Order Value Change vs Previous Month", "value": f"{average_order_value_change:.2f}%", "trend": "up" if average_order_value_change > 0 else "down"},
        {"title": "Total Orders Change vs Previous Month", "value": f"{total_orders_change:.2f}%", "trend": "up" if total_orders_change > 0 else "down"},
        {"title": "Sales Change vs Same Month Last Year", "value": f"{gmv_change_previous_year:.2f}%", "trend": "up" if gmv_change_previous_year > 0 else "down"},
        {"title": "Average Order Value Change vs Same Month Last Year", "value": f"{average_order_value_change_previous_year:.2f}%", "trend": "up" if average_order_value_change_previous_year > 0 else "down"},
        {"title": "Total Orders Change vs Same Month Last Year", "value": f"{total_orders_change_previous_year:.2f}%", "trend": "up" if total_orders_change_previous_year > 0 else "down"}
    ]

    st.markdown(f"""
    <div class="row">
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[0]["title"]}</h5>
            <p class="card-text">{card_data[0]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month else 'none'}">vs previous month: <span style="color: {'green' if card_data[3]['trend'] == 'up' else 'red'}" >{card_data[3]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[6]['trend'] == 'up' else 'red'}" >{card_data[6]["value"]}</span></div>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[1]["title"]}</h5>
            <p class="card-text">{card_data[1]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month else 'none'}">vs previous month: <span style="color: {'green' if card_data[4]['trend'] == 'up' else 'red'}" >{card_data[4]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[7]['trend'] == 'up' else 'red'}" >{card_data[7]["value"]}</span></div>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[2]["title"]}</h5>
            <p class="card-text">{card_data[2]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month else 'none'}">vs previous month: <span style="color: {'green' if card_data[5]['trend'] == 'up' else 'red'}" >{card_data[5]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[8]['trend'] == 'up' else 'red'}" >{card_data[8]["value"]}</span></div>
            </div>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_new_merchants_for_month(df, selected_month, selected_year):
    df_current_month = df[(df['brand_contacted_at_values'].dt.month == selected_month) & 
                          (df['brand_contacted_at_values'].dt.year == selected_year)]
    
    # if dataframe is empty
    if df_current_month.empty:
        return 0, 0, False
    else:

        # Filter rows where either 'first_order_for_brand_values' or 'very_first_order_for_brand_values' is True
        new_merchants_df = df_current_month[(df_current_month['first_order_for_brand_values'] == True) | (df_current_month['very_first_order_for_brand_values'] == True)]

        # marketplace merchants
        marketplace_merchants = new_merchants_df[new_merchants_df['sources'] == 'MARKETPLACE']

        # faire merchants
        faire_merchants = new_merchants_df[new_merchants_df['sources'] == 'ELEVATE']
        # count unique number of merchants
        total_new_marketplace_merchants = marketplace_merchants['retailer_tokens'].nunique()

        # count unique number of faire merchants
        total_new_faire_merchants = faire_merchants['retailer_tokens'].nunique()

        return total_new_marketplace_merchants, total_new_faire_merchants, True

def customer_acquisition_metrics(df, selected_month, selected_year, selected_month_string):

    # calculate new merchants for current month
    total_new_marketplace_merchants, total_new_faire_merchants, _ = get_new_merchants_for_month(df, selected_month, selected_year)

    # calculate new merchants for previous month
    total_new_marketplace_merchants_previous_month, total_new_faire_merchants_previous_month, display_previous_month = get_new_merchants_for_month(df, selected_month - 1, selected_year)

    # calculate new merchants for previous year
    total_new_marketplace_merchants_previous_year, total_new_faire_merchants_previous_year, display_previous_year = get_new_merchants_for_month(df, selected_month, selected_year - 1)

    # calculate percentage variation from current month to previous month
    percentage_variation_to_previous_month_marketplace = ((total_new_marketplace_merchants - total_new_marketplace_merchants_previous_month) / total_new_marketplace_merchants_previous_month) * 100 if total_new_marketplace_merchants_previous_month != 0 else 0
    percentage_variation_to_previous_month_faire = ((total_new_faire_merchants - total_new_faire_merchants_previous_month) / total_new_faire_merchants_previous_month) * 100 if total_new_faire_merchants_previous_month != 0 else 0

    # calculate percentage variation from current month to previous year
    percentage_variation_to_previous_year_marketplace = ((total_new_marketplace_merchants - total_new_marketplace_merchants_previous_year) / total_new_marketplace_merchants_previous_year) * 100 if total_new_marketplace_merchants_previous_year != 0 else 0
    percentage_variation_to_previous_year_faire = ((total_new_faire_merchants - total_new_faire_merchants_previous_year) / total_new_faire_merchants_previous_year) * 100 if total_new_faire_merchants_previous_year != 0 else 0

    # build card data
    card_data = [
        {"title": "New Marketplace Merchants", "value": f"{total_new_marketplace_merchants:,}"},
        {"title": "New Faire Merchants", "value": f"{total_new_faire_merchants:,}"},
        {"title": "New Marketplace Merchants Change vs Previous Month", "value": f"{percentage_variation_to_previous_month_marketplace:.2f}%", "trend": "up" if percentage_variation_to_previous_month_marketplace > 0 else "down"},
        {"title": "New Faire Merchants Change vs Previous Month", "value": f"{percentage_variation_to_previous_month_faire:.2f}%", "trend": "up" if percentage_variation_to_previous_month_faire > 0 else "down"},
        {"title": "New Marketplace Merchants Change vs Same Month Last Year", "value": f"{percentage_variation_to_previous_year_marketplace:.2f}%", "trend": "up" if percentage_variation_to_previous_year_marketplace > 0 else "down"},
        {"title": "New Faire Merchants Change vs Same Month Last Year", "value": f"{percentage_variation_to_previous_year_faire:.2f}%", "trend": "up" if percentage_variation_to_previous_year_faire > 0 else "down"}
    ]

    st.markdown(f"""
    <div class="row">
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[0]["title"]}</h5>
            <p class="card-text">{card_data[0]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month else 'none'}">vs previous month: <span style="color: {'green' if card_data[2]['trend'] == 'up' else 'red'}" >{card_data[2]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[4]['trend'] == 'up' else 'red'}" >{card_data[4]["value"]}</span></div>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[1]["title"]}</h5>
            <p class="card-text">{card_data[1]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month else 'none'}">vs previous month: <span style="color: {'green' if card_data[3]['trend'] == 'up' else 'red'}" >{card_data[3]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[5]['trend'] == 'up' else 'red'}" >{card_data[5]["value"]}</span></div>
            </div>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def get_value_marketing_campaigns_for_month(df, selected_month, selected_year, type_action):
    # Filter rows based on start month and year
    target_campaigns = df[(df['start_sending_at'].dt.month == selected_month) &
                                        (df['start_sending_at'].dt.year == selected_year)]
    
    # if dataframe is empty
    if target_campaigns.empty:
        return 0, False
    else:
        # Sum the type_action for the filtered campaigns
        total_order_value_sum = target_campaigns[type_action].sum()
        return total_order_value_sum, True
    
def get_marketing_campaign_sales(df, selected_month, selected_year):

    # calculate total sales for current month
    total_sales_open, _ = get_value_marketing_campaigns_for_month(df, selected_month, selected_year, "open_based_total_order_value")
    total_sales_click, _ = get_value_marketing_campaigns_for_month(df, selected_month, selected_year, "click_based_total_order_value")

    # calculate total sales for previous month
    total_sales_open_previous_month, display_previous_month_open = get_value_marketing_campaigns_for_month(df, selected_month - 1, selected_year, "open_based_total_order_value")
    total_sales_click_previous_month, display_previous_month_click = get_value_marketing_campaigns_for_month(df, selected_month - 1, selected_year, "click_based_total_order_value")

    # calculate total sales for previous year
    total_sales_open_previous_year, display_previous_year_open = get_value_marketing_campaigns_for_month(df, selected_month, selected_year - 1, "open_based_total_order_value")
    total_sales_click_previous_year, display_previous_year_click = get_value_marketing_campaigns_for_month(df, selected_month, selected_year - 1, "click_based_total_order_value")

    # calculate percentage variation from current month to previous month
    percentage_variation_to_previous_month_open = ((total_sales_open - total_sales_open_previous_month) / total_sales_open_previous_month) * 100 if total_sales_open_previous_month != 0 else 0
    percentage_variation_to_previous_month_click = ((total_sales_click - total_sales_click_previous_month) / total_sales_click_previous_month) * 100 if total_sales_click_previous_month != 0 else 0

    # calculate percentage variation from current month to previous year
    percentage_variation_to_previous_year_open = ((total_sales_open - total_sales_open_previous_year) / total_sales_open_previous_year) * 100 if total_sales_open_previous_year != 0 else 0
    percentage_variation_to_previous_year_click = ((total_sales_click - total_sales_click_previous_year) / total_sales_click_previous_year) * 100 if total_sales_click_previous_year != 0 else 0

    # build card_data
    card_data = [
        {"title": "Total Sales Open emails", "value": f"${total_sales_open:,.2f}"},
        {"title": "Total Sales Click emails", "value": f"${total_sales_click:,.2f}"},
        {"title": "Total Sales Open emails Change vs Previous Month", "value": f"{percentage_variation_to_previous_month_open:.2f}%", "trend": "up" if percentage_variation_to_previous_month_open > 0 else "down"},
        {"title": "Total Sales Click emails Change vs Previous Month", "value": f"{percentage_variation_to_previous_month_click:.2f}%", "trend": "up" if percentage_variation_to_previous_month_click > 0 else "down"},
        {"title": "Total Sales Open emails Change vs Same Month Last Year", "value": f"{percentage_variation_to_previous_year_open:.2f}%", "trend": "up" if percentage_variation_to_previous_year_open > 0 else "down"},
        {"title": "Total Sales Click emails Change vs Same Month Last Year", "value": f"{percentage_variation_to_previous_year_click:.2f}%", "trend": "up" if percentage_variation_to_previous_year_click > 0 else "down"}
    ]

    st.markdown(f"""
    <div class="row">
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[0]["title"]}</h5>
            <p class="card-text">{card_data[0]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month_open else 'none'}">vs previous month: <span style="color: {'green' if card_data[2]['trend'] == 'up' else 'red'}" >{card_data[2]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year_open else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[4]['trend'] == 'up' else 'red'}" >{card_data[4]["value"]}</span></div>
            </div>
        </div>
        </div>
        <div class="col">
        <div class="card">
            <div class="card-body">
            <h5 class="card-title">{card_data[1]["title"]}</h5>
            <p class="card-text">{card_data[1]["value"]}</p>
            <div class="divider-line" ></div>
            <div style="display: {'block' if display_previous_month_click else 'none'}">vs previous month: <span style="color: {'green' if card_data[3]['trend'] == 'up' else 'red'}" >{card_data[3]["value"]}</span></div>
            <div style="display: {'block' if display_previous_year_click else 'none'}" >vs same month last year: <span style="color: {'green' if card_data[5]['trend'] == 'up' else 'red'}" >{card_data[5]["value"]}</span></div>
            </div>
        </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    