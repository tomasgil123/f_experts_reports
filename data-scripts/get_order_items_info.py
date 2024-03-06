import pandas as pd

def create_empty_order_items_df():
    # we create a dataframe with the columns we want
    order_items_df = pd.DataFrame(columns=["token", "order_token", "product_token", "brand_order_token", "product_name", "product_option_name", "suggested_retail_price", "retailer_price", "retailer_original_price", "total_retailer_price", "retailer_total", "discount_percentage", "localized_brand_order_number", "product_variations"])
    return order_items_df

def get_order_items_info(order_items):

    # Initialize lists to store specific order attributes
    oi_tokens = []
    oi_order_tokens = []
    oi_product_tokens = []
    oi_brand_order_tokens = []
    oi_product_names = []
    oi_product_option_names = []
    oi_suggested_retail_prices = []
    oi_retailer_prices = []
    oi_retailer_original_prices = []
    oi_total_retailer_prices = []
    oi_retailer_totals = []
    oi_discount_percentages = []
    oi_localized_brand_order_number = []
    oi_product_variations = []

    # we iterate over order_items and get the order items info
    for order_item in order_items:
        oi_tokens.append(order_item["token"])
        oi_order_tokens.append(order_item["order_token"])
        oi_product_tokens.append(order_item["product_token"])
        oi_brand_order_tokens.append(order_item["brand_order_token"])
        oi_product_names.append(order_item["product_name"])
        oi_product_option_names.append(order_item["product_option_name"])
        oi_suggested_retail_prices.append(order_item["suggested_retail_price"]["amount_cents"])
        oi_retailer_prices.append(order_item["retailer_price"]["amount_cents"])
        oi_retailer_original_prices.append(order_item["retailer_original_price"]["amount_cents"])
        oi_total_retailer_prices.append(order_item["total_retailer_price"]["amount_cents"])
        oi_retailer_totals.append(order_item["retailer_total"]["amount_cents"])
        oi_discount_percentages.append(order_item["discount_percentage"])
        oi_localized_brand_order_number.append(order_item["localized_brand_order_number"])
        # if product variations is not an empty list, we append array info as a string to product_variations
        if order_item["product_variations"]:
            oi_product_variations.append(str(order_item["product_variations"]))
        else:
            oi_product_variations.append("")

    # we create a dataframe with the order items info
    order_items_df = pd.DataFrame({
        "token": oi_tokens,
        "order_token": oi_order_tokens,
        "product_token": oi_product_tokens,
        "brand_order_token": oi_brand_order_tokens,
        "product_name": oi_product_names,
        "product_option_name": oi_product_option_names,
        "suggested_retail_price": oi_suggested_retail_prices,
        "retailer_price": oi_retailer_prices,
        "retailer_original_price": oi_retailer_original_prices,
        "total_retailer_price": oi_total_retailer_prices,
        "retailer_total": oi_retailer_totals,
        "discount_percentage": oi_discount_percentages,
        "localized_brand_order_number": oi_localized_brand_order_number,
        "product_variations": oi_product_variations
    })

    return order_items_df
    


