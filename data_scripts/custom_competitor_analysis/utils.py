import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _fbp=fb.1.1709731797476.527673433; _gcl_au=1.1.1527690070.1712605646; _ga_09CCX15SCN=GS1.1.1712605706.15.1.1712606145.0.0.0; _ga=GA1.2.1582770238.1704718676; _cfuvid=tK225n5z24nKIxycb_wu5CSIl3KAh0hKdcmUx07og6g-1713176577406-0.0.1.1-604800000; IR_gbd=faire.com; __hssrc=1; _gid=GA1.2.1271584729.1713470552; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjEsInR5cCI6IkpXVCJ9.eyJzIjoiZGI4eWZ3MnZ5YnMwNm96YnhkcWRpeTBpbjJ0ODhyOHA5dHk4bjEwOTl2aDB2MzdjYTYycXc3YmJ4bmp4OHRrOGp4ajR3NG9samJrNXpyN3VpeXh3OWlwcGptdGdwOHhpMW0ydSIsImQiOjE3MTM1MzU2OTMsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiXV0sInUiOiJ1X2VhZ3FobXdjZmUiLCJmIjoiYzZoZzM2ZHJoNXkwdmVsaXBhdHE5aHM0ajhuZGJ3OGhibXFxcGlmOThzeTk0dWhrazhkc2dldG9ocDR4d3FyZnJ6ZjQ1cmViMmd3MnJpaG1ueTZzYTN2bThvOTZxbmJnbjA0byIsInYiOjE3MTM1MzU2OTMsImwiOiJlbiJ9.D7mC2jr8e0ENzguH79m_PkxTQsnYhrbo00ABQkG5WKtMhx6TnBS63Snwxt3WPyzQ3LRxt3TVFksqGBpcIq0SFICm0EkzizRocUy21FzAecsvFEJZJ1pu9SleWaNHx2uNhhParzLF1MQEx9P9wm7UgLZHftGQCSuEqxKwS4EeWWLZkiNWGhb4kcfYu2lHxCzd7uZByEcPJhnj9lhnt9rDJE1cupX6h320K2BM3whU6WctG19sda1A0u-9xDcyaeVFO0dIJpykKvlyIO53RwYK76sfCUM1en-BNGDJMMLtuvPSgv4iYi1VM5hbzeT5hJPtubcGYy9jW0YhF5sWfz5VEw; __cf_bm=MrNJfTDNKhYwbqHidubHZJ0MicU0CmReMojDwFe3Ys4-1713535693-1.0.1.1-cx2vI79XvmdoI.hDjCFsNPAxM.7BJDbRpksoFYza4CGpk5AkZjAK6Dz5pDBK03yyuwUUscTWtPZkbBqaaZN68g; _hjSession_3000850=eyJpZCI6ImE3YjNjMTMwLWE4NGUtNDc2OC1hZWNjLWRmM2I2NTkyMzBkNSIsImMiOjE3MTM1MzU3MDEzOTYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1713470552265.1713535701772.114; __hssc=62287155.1.1713535701772; _gat_UA-90386801-1=1; IR_21072=1713535795262%7C0%7C1713535795262%7C%7C; _uetsid=975554e0fdbe11ee9a2e63ccb82ac8ff; _uetvid=d86963a0474811eeb792fb4adaaa7106; _ga_3FHCRNP43E=GS1.2.1713535701.111.1.1713535795.40.0.0; _derived_epik=dj0yJnU9cWQxdmJfWEN4RmFpOXFrMW1peFJkUHZITmJpS1ZsamQmbj1QMWh4U1E4eW5ZY2ZKbUw3d0h4S3ZnJm09MSZ0PUFBQUFBR1lpZXpNJnJtPTEmcnQ9QUFBQUFHWWllek0mc3A9Mg"

def get_products_info_page(page_number, brand_token, cookie, filter_keys, type_search="filter"):
    # Define the API endpoint URL
    endpoint_url = "https://www.faire.com/api/v2/search/products/from-brand"

    # Define the payload data for the POST request
    if type_search == "filter":
        payload = {
            "filter_keys": filter_keys,
            "brand_token": brand_token,
            "page_number": page_number,
            "page_size": 100
        }
    else:
        payload = {
            "filter_keys": [],
            "brand_token": brand_token,
            "page_number": page_number,
            "query": filter_keys,
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
    wholesale_promo_prices = []
    badge_list = []

    page_count = 0

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
                    if "min_option_wholesale_promo_price" not in product_tile:
                        wholesale_promo_prices.append(0)
                    else:
                        wholesale_promo_prices.append(product_tile["min_option_wholesale_promo_price"]["discount_bps"] / 100)
                    
                    # we get badges (Bestseller, Brand Bestseller, Trending, New, etc.)
                    badges = product_tile["badge_list"]["badges"]
                    # we check if len is bigger than 0
                    if len(badges) > 0:
                        badge_list_string = ""
                        # we loop through the badges
                        for badge in badges:
                            # if string is empty
                            if badge_list_string == "":
                                badge_list_string = badge["type"]
                            else:
                                badge_list_string = badge_list_string + " | " + badge["type"]
                        badge_list.append(badge_list_string)
                    else:
                        badge_list.append("")

                print("after product tiles")
                break  # Successful request, exit the loop
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/{max_retries})")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                #print("product", product)
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            #print("product", product)
            print(f"An error occurred: {e}")
            break  # Exit the loop on other exceptions
    return product_names, is_new_list, product_tokens, product_states, retail_prices, wholesale_prices, wholesale_promo_prices, badge_list, page_count
