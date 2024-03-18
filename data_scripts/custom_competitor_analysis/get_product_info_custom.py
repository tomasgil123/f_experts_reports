import pandas as pd
import time

from utils import (cookie_token, get_products_info_page)

def get_products_info(brand_owner):
    # we create a dataframe using the brands_competitors csv
    df_brands = pd.read_csv('brands_competitors.csv')

    # we filter the dataframe to get the brands for each brand_owner
    df_brands_filtered = df_brands[df_brands['brand_owner'] == brand_owner]

    brand_id = []
    product_category = []
    product_names = []
    is_new_list = []
    product_tokens = []
    product_states = []
    retail_prices = []
    wholesale_prices = []
    wholesale_promo_prices = []
    badge_list = []

    # we loop through the brands list
    for brand in df_brands_filtered.to_dict('records'):
        print("brand", brand)

        categories = brand["categories"].split('|')
        type_search = brand["type_search"]

        # we loop through the categories
        for category in categories:

            if type_search == "filter":
                filter_string = "taxonomy_type:" + category
                filter_keys = [filter_string]
            else:
                filter_keys = category
            
            page_number = 1
            brand_token = brand["brand_id"]
            cookie = cookie_token()
            print(f"page 1 for category {category}")
            product_names_page, is_new_list_page, product_tokens_page, product_states_page, retail_prices_page, wholesale_prices_page, wholesale_promo_prices_page, badge_list_page, page_count = get_products_info_page(page_number, brand_token, cookie, filter_keys, type_search)
            
            brand_id.extend([brand_token for i in range(len(product_names_page))])
            product_category.extend([category.title() for i in range(len(product_names_page))])
            product_names.extend(product_names_page)
            is_new_list.extend(is_new_list_page)
            product_tokens.extend(product_tokens_page)
            product_states.extend(product_states_page)
            retail_prices.extend(retail_prices_page)
            wholesale_prices.extend(wholesale_prices_page)
            wholesale_promo_prices.extend(wholesale_promo_prices_page)
            badge_list.extend(badge_list_page)
            time.sleep(10)

            if page_count > 1:
                for page in range(2, page_count + 1):
                    print(f"page {page}/{page_count} for category {category}")
                    product_names_page, is_new_list_page, product_tokens_page, product_states_page, retail_prices_page, wholesale_prices_page, wholesale_promo_prices_page, badge_list_page, _ = get_products_info_page(page, brand_token, cookie, filter_keys, type_search)
                    
                    brand_id.extend([brand_token for i in range(len(product_names_page))])
                    product_category.extend([category for i in range(len(product_names_page))])
                    product_names.extend(product_names_page)
                    is_new_list.extend(is_new_list_page)
                    product_tokens.extend(product_tokens_page)
                    product_states.extend(product_states_page)
                    retail_prices.extend(retail_prices_page)
                    wholesale_prices.extend(wholesale_prices_page)
                    wholesale_promo_prices.extend(wholesale_promo_prices_page)
                    badge_list.extend(badge_list_page)
                    time.sleep(10)
    
    # we create a data object
    data = {
        "Brand ID": brand_id,
        "Product Category": product_category,
        "Product Name": product_names,
        "Is New": is_new_list,
        "Product Token": product_tokens,
        "Product State": product_states,
        "Retail Price": retail_prices,
        "Wholesale Price": wholesale_prices,
        "Wholesale Promo Discount Percentage": wholesale_promo_prices,
        "Badge List": badge_list
    }
    return data

            
    

    
