import streamlit as st
import requests
import pandas as pd

def get_competitors_brand_data():
    headers = {
        'User-Agent': 'insomnia/8.6.0'
    }
    brand_ids =["b_3dzktmhtkw", "b_arceup81f2", "b_40j19ly1ct", "b_bp6yz427jb", "b_ebdxha3tko"]
    # Initialize an empty list to store responses
    responses_brand_data = []

    # Iterate over each brand ID and make a request
    for brand_id in brand_ids:
        url = f"https://www.faire.com/api/v2/brand-view/{brand_id}"
        response = requests.get(url, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            responses_brand_data.append(response.json())
        else:
            print(f"Failed to fetch data for brand ID {brand_id}")
    
    # Define empty lists to store the extracted information
    brand_names = []
    average_ratings = []
    number_of_reviews = []
    minimum_order_amounts = []

    # Iterate through the brand_list and extract the required information
    for brand_data in responses_brand_data:
        brand = brand_data["brand"]
        brand_names.append(brand["name"])
        
        # Extract review info
        average_ratings.append(brand["brand_reviews_summary"]["average_rating"])
        number_of_reviews.append(brand["brand_reviews_summary"]["number_of_reviews"])
        
        # Extract minimum order info
        minimum_order_amounts.append(brand["minimum_order_amount"]["amount_cents"] / 100)  # Convert cents to dollars

    # Create a DataFrame using the extracted information
    data = {
        "Brand Name": brand_names,
        "Average Rating": average_ratings,
        "Number of Reviews": number_of_reviews,
        "Minimum Order Amount (USD)": minimum_order_amounts
    }

    brand_df = pd.DataFrame(data)
    st.dataframe(brand_df)

def competitor_analysis():

    st.markdown("<p style='font-weight: bold;' class='body-text'>Major Competitors:</p>", unsafe_allow_html=True)
    
    text_brands = ["Sarta", "Roma Leathers (Top Shop)", "Sixtease Bags USA", "Threaded Pair"]
    # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in text_brands:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Product Optimization Strategies:</p>", unsafe_allow_html=True)

        # Texts
    texts_opt_strategies = [
        "Enhance Product Titles: Incorporate ‘Handcrafted’ into product names to emphasize craftsmanship.",
        "Highlight Media Recognition: Showcase publications where Latico has been featured, enhancing brand credibility.",
        "Leverage Awards: Use ‘award-winning’ in product descriptions to underline quality and distinction.",
        "Seasonal Marketing Focus: Utilize holiday-themed keywords in collection names, email campaign subjects, and content to drive seasonal sales."
    ]

    # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in texts_opt_strategies:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Review Analysis:</p>", unsafe_allow_html=True)

    text_reviews = ["General Trends: Most competitors have over 30 reviews.", 
                    "Notable Exception: Threaded Pair stands out with over 450 reviews.", 
                    "Rating Overview: All competitors maintain high ratings, averaging above 4.8 stars."]
    
     # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in text_reviews:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Brand Attributes:</p>", unsafe_allow_html=True)

    text_brand_attributes = ["Key Differentiators: Eco-Friendly", "Women-Owned", "Exclusive to Faire (Not on Amazon)", "Handmade Products", "Charitable Contributions"]

    # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in text_brand_attributes:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Key Market Insights:</p>", unsafe_allow_html=True)

    text_market_insights = ["Pricing Strategy: Competitors generally offer products at a lower price point, likely making them more accessible to a wider audience.",
                            "Suggestion: Consider revising Latico’s pricing strategy to be more competitive, particularly for entry-level products.",
                            "Brand Minimums: Latico’s current minimum order value is significantly higher ($500) compared to competitors, who range between $100-$300.",
                            "Recommendation: Lower the minimum order value to align more closely with market standards. This could enhance accessibility and appeal to a broader customer base.",
                            "Customer Engagement: Proactively engage with customers to encourage more 5-star reviews, enhancing the brand’s reputation and trustworthiness."]
    
    # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in text_market_insights:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown("<p style='font-weight: bold;' class='body-text'>Action Plan:</p>", unsafe_allow_html=True)

    text_action_plan = ["Revisit Pricing Strategy: Conduct a detailed analysis of product pricing compared to competitors. Consider adjustments to be more competitive while maintaining profit margins.",
                        "Minimum Order Adjustment: Explore the feasibility of lowering the minimum order value. Analyze the potential impact on sales volume and customer acquisition.",
                        "Enhance Customer Engagement: Develop a strategy for increasing customer reviews and feedback, possibly through post-purchase follow-ups or incentives for reviewing products."]
    
    # Render a ul list with each text as an li element using st.markdown
    st.markdown("<ul class='body-text'>", unsafe_allow_html=True)
    for text in text_action_plan:
        st.markdown(f"<li>{text}</li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)