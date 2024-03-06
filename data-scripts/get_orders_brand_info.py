
# token, creation_reason, source, brand_contacted_at, first_order_for_brand, very_first_order_for_brand, 
# retailer_token, payout_total (amount_cents)

import requests
import time

def get_orders_info_page(page_number, brand_token, cookie):
    endpoint_url = "https://www.faire.com/api/v2/brand-orders/list"

    payload = {
        "states": [],
        "brand_token": brand_token,
        "type_filter": "ALL",
        "page": page_number,
        "page_size": 100,
        "sort_by": "CREATED_AT",
        "sort_order": "DESC"
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    # Initialize lists to store specific order attributes
    tokens = []
    creation_reasons = []
    states = []
    fulfillment_states = []
    sources = []
    brand_contacted_at_values = []
    first_order_for_brand_values = []
    very_first_order_for_brand_values = []
    retailer_tokens = []
    payout_total_values = []
    retailer_names = []
    retailer_website_urls = []
    retailer_store_types = []

    page_count = 1

    retry_count = 0

    while retry_count < 3:
        try:
            # Make the POST request to the API
            response = requests.post(endpoint_url, json=payload, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                page_count = data["pagination_data"]["page_count"]

                # Loop through the order tiles
                for order in data["brand_orders"]:
                    order_token = order["token"]
                    tokens.append(order_token)
                    creation_reasons.append(order["creation_reason"])
                    states.append(order["state"])
                    fulfillment_states.append(order["fulfillment_state"])
                    sources.append(order["source"])
                    brand_contacted_at_values.append(order["brand_contacted_at"])
                    first_order_for_brand_values.append(order["first_order_for_brand"])
                    # if the key very_first_order_for_brand is not present, we append None
                    if "very_first_order_for_brand" not in order:
                        very_first_order_for_brand_values.append(None)
                    else:
                        very_first_order_for_brand_values.append(order["very_first_order_for_brand"])
                    retailer_tokens.append(order["retailer_token"])
                    payout_total_values.append(order["payout_total"]["amount_cents"])

                    # we get retailers data
                    retailer_names.append(data["brand_order_tokens_to_retailer_names"][order_token])
                    retailer_details = data["brand_order_tokens_to_retailer_details"][order_token]
                    if "website_url" in retailer_details:
                        retailer_website_urls.append(retailer_details["website_url"])
                    else:
                        retailer_website_urls.append(None)
                    # if store_type exist, we add it to the list. Otherwise we add None
                    if "store_type" in retailer_details:
                        retailer_store_types.append(retailer_details["store_type"])
                    else:
                        retailer_store_types.append(None)
                

                break  # Successful request, exit the loop
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/3)")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    print(f"Page {page_number} of {page_count} processed")
    return tokens, creation_reasons, sources, brand_contacted_at_values, first_order_for_brand_values, very_first_order_for_brand_values, retailer_tokens, payout_total_values, states, fulfillment_states, retailer_names, retailer_website_urls, retailer_store_types, page_count

def get_orders_info(brand_token, cookie):
    # Initialize lists to store the specific order attributes
    tokens = []
    creation_reasons = []
    sources = []
    states = []
    fulfillment_states = []
    brand_contacted_at_values = []
    first_order_for_brand_values = []
    very_first_order_for_brand_values = []
    retailer_tokens = []
    payout_total_values = []
    retailer_names = []
    retailer_website_urls = []
    retailer_store_types = []

    # we loop over the different pages and get the orders info
    page_number = 1
    tokens_page, creation_reasons_page, sources_page, brand_contacted_at_values_page, first_order_for_brand_values_page, very_first_order_for_brand_values_page, retailer_tokens_page, payout_total_values_page, states_page, fulfillment_states_page, retailer_names_page, retailer_website_urls_page, retailer_store_types_page, page_count  =  get_orders_info_page(page_number, brand_token, cookie)
    time.sleep(10)
    tokens.extend(tokens_page)
    creation_reasons.extend(creation_reasons_page)
    states.extend(states_page)
    fulfillment_states.extend(fulfillment_states_page)
    sources.extend(sources_page)
    brand_contacted_at_values.extend(brand_contacted_at_values_page)
    first_order_for_brand_values.extend(first_order_for_brand_values_page)
    very_first_order_for_brand_values.extend(very_first_order_for_brand_values_page)
    retailer_tokens.extend(retailer_tokens_page)
    payout_total_values.extend(payout_total_values_page)
    retailer_names.extend(retailer_names_page)
    retailer_website_urls.extend(retailer_website_urls_page)
    retailer_store_types.extend(retailer_store_types_page)

    # we loop over the different pages and get the orders info
    if page_count > 1:
        for page_number in range(2, page_count + 1):
            tokens_page, creation_reasons_page, sources_page, brand_contacted_at_values_page, first_order_for_brand_values_page, very_first_order_for_brand_values_page, retailer_tokens_page, payout_total_values_page, states_page, fulfillment_states_page,retailer_names_page, retailer_website_urls_page, retailer_store_types_page, _ =  get_orders_info_page(page_number, brand_token, cookie)
            time.sleep(10)
            tokens.extend(tokens_page)
            creation_reasons.extend(creation_reasons_page)
            states.extend(states_page)
            fulfillment_states.extend(fulfillment_states_page)
            sources.extend(sources_page)
            brand_contacted_at_values.extend(brand_contacted_at_values_page)
            first_order_for_brand_values.extend(first_order_for_brand_values_page)
            very_first_order_for_brand_values.extend(very_first_order_for_brand_values_page)
            retailer_tokens.extend(retailer_tokens_page)
            payout_total_values.extend(payout_total_values_page)
            retailer_names.extend(retailer_names_page)
            retailer_website_urls.extend(retailer_website_urls_page)
            retailer_store_types.extend(retailer_store_types_page)

    data = {
        "tokens": tokens,
        "creation_reasons": creation_reasons,
        "states": states,
        "fulfillment_states": fulfillment_states,
        "sources": sources,
        "brand_contacted_at_values": brand_contacted_at_values,
        "first_order_for_brand_values": first_order_for_brand_values,
        "very_first_order_for_brand_values": very_first_order_for_brand_values,
        "retailer_tokens": retailer_tokens,
        "payout_total_values": payout_total_values,
        "retailer_names": retailer_names,
        "retailer_website_urls": retailer_website_urls,
        "retailer_store_types": retailer_store_types
    }

    return data




