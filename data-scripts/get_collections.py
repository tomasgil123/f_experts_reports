import requests
import time

def get_collections_info_for_brand(brand_token, cookie):
    
    endpoint_url = f"https://www.faire.com/api/brand/{brand_token}/published-product-collection-metadata"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    collection_title = []
    created_at = []
    updated_at = []
    total_items = []
    collection_promo = []
    collection_promo_discount = []
    collection_promo_started_at = []

    # we will retry the request 3 times if it fails

    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        try:
            # Make the GET request to the API
            response = requests.get(endpoint_url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                # Loop through the product tiles
                for collection in data["product_based_collections"]:
                    collection_title.append(collection["name"])
                    created_at.append(collection["created_at"])
                    updated_at.append(collection["updated_at"])
                    total_items.append(collection["total_items"])
                    # we check if there is a collection_promo
                    if "collection_promo" in collection:
                        collection_promo.append(1)
                        collection_promo_discount.append(collection["collection_promo"]["discount_bps"])
                        collection_promo_started_at.append(collection["collection_promo"]["started_at"])
                    else:
                        collection_promo.append(0)
                        collection_promo_discount.append(0)
                        collection_promo_started_at.append(0)
                
                break  # Exit the loop on success
                
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/{max_retries})")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            print(f"Request failed with exception: {e}")
            break

    data = {
        "collection_title": collection_title,
        "created_at": created_at,
        "updated_at": updated_at,
        "total_items": total_items,
        "collection_promo": collection_promo,
        "collection_promo_discount": collection_promo_discount,
        "collection_promo_started_at": collection_promo_started_at
    }

    return data