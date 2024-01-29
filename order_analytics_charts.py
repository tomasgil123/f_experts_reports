import streamlit as st
import pandas as pd
from datetime import datetime

def lifetime_performance_metrics(data):
    st.markdown("<h1 class='title-text'>Total sales, average order value and orders</h1>", unsafe_allow_html=True)
    st.markdown("<p class='body-text'>Only orders with status 'Delivered' or 'Shipped' were considered.</p>", unsafe_allow_html=True)
    
    # Keep only orders with status "Shipped" or "Delivered"
    data = data[data['Status'].isin(['Shipped', 'Delivered'])]
    # Filter data for the last 12 months
    last_12_months = data[data['Order Date'] >= (datetime.now() - pd.DateOffset(months=12))]

    # Filter data for the last 3 months
    last_3_months = data[data['Order Date'] >= (datetime.now() - pd.DateOffset(months=3))]

    # Calculate metrics for the last 12 months
    total_sales_12_months = last_12_months['Wholesale Price'].sum()
    average_order_value_12_months = total_sales_12_months / last_12_months['Order Number'].nunique()
    number_of_orders_12_months = last_12_months['Order Number'].nunique()

    # Calculate metrics for the last 3 months
    total_sales_3_months = last_3_months['Wholesale Price'].sum()
    average_order_value_3_months = total_sales_3_months / last_3_months['Order Number'].nunique()
    number_of_orders_3_months = last_3_months['Order Number'].nunique()
    
    card_data = [
        {"title": "Total Sales", "value": f"${total_sales_12_months:,.2f}"},
        {"title": "Average Order Value", "value": f"${average_order_value_12_months:,.2f}"},
        {"title": "Number of Orders", "value": f"{number_of_orders_12_months:,}"},
        {"title": "Total Sales", "value": f"${total_sales_3_months:,.2f}"},
        {"title": "Average Order Value", "value": f"${average_order_value_3_months:,.2f}"},
        {"title": "Number of Orders", "value": f"{number_of_orders_3_months:,}"}
    ]
    st.markdown("<p style='font-weight: bold;' class='body-text'>Last 12 months:</p>", unsafe_allow_html=True)
    # First Row
    st.markdown(f"""
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
    """, unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Last 3 months:</p>", unsafe_allow_html=True)
    # Second row
    st.markdown(f"""
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

