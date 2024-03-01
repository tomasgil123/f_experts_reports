import requests
import time

def get_product_categories(brand_token, cookie):
    endpoint_url = "https://www.faire.com/api/v2/search/products/from-brand/filters"

    # Define the payload data for the POST request
    payload = {
        "filter_keys": [],
        "brand_token": brand_token,
        "client_size": "DESKTOP"
    }
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    # Make the POST request to the API
    response = requests.post(endpoint_url, json=payload, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()

        category_filter_section = [obj for obj in data["filter_sections"] if obj["field_name"] == "TAXONOMY_TYPE"] 

        product_categories = category_filter_section[0]["options"]

        return product_categories

        

def get_products_info_page(page_number, brand_token, cookie, filter_keys):
    # Define the API endpoint URL
    endpoint_url = "https://www.faire.com/api/v2/search/products/from-brand"

    # Define the payload data for the POST request
    payload = {
        "filter_keys": filter_keys,
        "brand_token": brand_token,
        "page_number": page_number,
        "page_size": 100
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    # Initialize lists to store the specific product attributes
    product_names = []
    is_new_list = []
    product_tokens = []
    product_states = []
    retail_prices = []
    wholesale_prices = []

    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        print(f"Fetching page {page_number} (Retry {retry_count + 1}/{max_retries})")
        try:
            # Make the POST request to the API
            response = requests.post(endpoint_url, json=payload, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                page_count = data["pagination_data"]["page_count"]

                # Loop through the product tiles
                for product_tile in data["product_tiles"]:
                    product = product_tile["product"]
                    product_names.append(product["name"])
                    is_new_list.append(product["is_new"])
                    product_tokens.append(product["token"])
                    product_states.append(product["state"])
                    # if product doesn't have key "min_option_retail_price" or "min_option_wholesale_price" we append 0
                    if "min_option_retail_price" not in product_tile:
                        retail_prices.append(0)
                    else:
                        retail_prices.append(product_tile["min_option_retail_price"]["amount_cents"] / 100)
                    if "min_option_wholesale_price" not in product_tile:
                        wholesale_prices.append(0)
                    else:
                        wholesale_prices.append(product_tile["min_option_wholesale_price"]["amount_cents"] / 100)
                print("after product tiles")
                break  # Successful request, exit the loop
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/{max_retries})")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                print("product", product)
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            print("product", product)
            print(f"An error occurred: {e}")
            break  # Exit the loop on other exceptions
    print('end getting product info', product_names)
    return product_names, is_new_list, product_tokens, product_states, retail_prices, wholesale_prices, page_count

def get_products_info(brand_token, cookie):
    
    # Get all the product categories
    product_categories = get_product_categories(brand_token, cookie)
    time.sleep(10)  # Sleep for 30 seconds between requests

    # Initialize lists to store the specific product attributes
    product_category = []
    product_names = []
    is_new_list = []
    product_tokens = []
    product_states = []
    retail_prices = []
    wholesale_prices = []

    # Loop through the product categories
    for category in product_categories:
        filter_keys = [category["key"]]
        page_number = 1
        product_names_page, is_new_list_page, product_tokens_page, product_states_page, retail_prices_page, wholesale_prices_page, page_count = get_products_info_page(page_number, brand_token, cookie, filter_keys)
        product_category.extend([category["display_name"] for i in range(len(product_names_page))])
        product_names.extend(product_names_page)
        is_new_list.extend(is_new_list_page)
        product_tokens.extend(product_tokens_page)
        product_states.extend(product_states_page)
        retail_prices.extend(retail_prices_page)
        wholesale_prices.extend(wholesale_prices_page)
        time.sleep(10)  # Sleep for 30 second between requests

        if page_count > 1:
            for page in range(2, page_count + 1):
                print(f"Fetching page {page}/{page_count} for category {category['display_name']}")
                print("---------")
                product_names_page, is_new_list_page, product_tokens_page, product_states_page, retail_prices_page, wholesale_prices_page, _ = get_products_info_page(page, brand_token, cookie, filter_keys)
                product_category.extend([category["display_name"] for i in range(len(product_names_page))])
                print("after request")
                product_names.extend(product_names_page)
                is_new_list.extend(is_new_list_page)
                product_tokens.extend(product_tokens_page)
                product_states.extend(product_states_page)
                retail_prices.extend(retail_prices_page)
                wholesale_prices.extend(wholesale_prices_page)
                time.sleep(10)  # Sleep for 30 second between requests

    data = {
        "Product Category": product_category,
        "Product Name": product_names,
        "Is New": is_new_list,
        "Product Token": product_tokens,
        "Product State": product_states,
        "Retail Price": retail_prices,
        "Wholesale Price": wholesale_prices
    }

    return data



        