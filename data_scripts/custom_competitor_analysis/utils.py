import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; _cfuvid=xB0NYVVvwCOlKj1pqDPdIVPbXXYd_DykKVPcc_xvzE0-1718465296721-0.0.1.1-604800000; _gid=GA1.2.1931496025.1718576362; _ga_09CCX15SCN=GS1.1.1718660044.20.0.1718660046.0.0.0; _ga=GA1.2.1582770238.1704718676; faire_mfa_suppression_secret=4golr5xw9niid20t5y92o0r9rdfl87qgigvbcc50tj; _hjSession_3000850=eyJpZCI6ImRjOGZkYTFiLTk0ZjEtNGUwZC05NGFlLTI2MjFhMDNiNjUzMiIsImMiOjE3MTg3MzE1NjA1OTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1718724350280.1718731565096.176; cf_clearance=rd0wqkzZ5Q6xompBVU3Rbt3Wg1aUdt6eDTHqyqETcL8-1718733773-1.0.1.1-ucu3GFK_vLu_tbXArsvUrb0URg2Qct8bjTahbCNC7r_b5roFxt6vQlD.4dxSZnq4Kt2sJpa3hU_1HgkXoWq3Zg; _uetsid=70ce4f202d7611ef9bacab490a79c606; _uetvid=d86963a0474811eeb792fb4adaaa7106; _derived_epik=dj0yJnU9QTBMZlFkM29OZG0tSjR6SXhubDFUS0Q4QUIwX1hpOV8mbj15dExIazNkMXF1M1k1LXYyclJvaFV3Jm09ZiZ0PUFBQUFBR1p4ejFNJnJtPWYmcnQ9QUFBQUFHWnh6MU0mc3A9Mg; IR_21072=1718734675643%7C0%7C1718734675643%7C%7C; __hssc=62287155.15.1718731565096; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiYzNoMGtxM3Z3bzQzMnRheXVvYXdscWdpdTZ3NnFrbjhiMTdscDUxbWtjdHQxN3ZrYnAzZGM1NDNkazd3NTV5dG1wbGNsYmw2Znh6YmFmY2VheG05cDZkcnZ2a3ppdGo0cTNtaCIsImQiOjE3MTg3MzQ5NzQsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzE4NzMyNzMyLCJsIjoiZW4ifQ.rL1O6VtguNzRFJLDSVkb3Em4hLF5dQNucgEAtOfKP79t9Gx4UdtozxGdDKlhK71GgzY-OVhy692LGW9TrLMVLSxGqFe729TokRnQXvoh4V4S77inHbrFe3nJY89G8v0qAFk9qXpPt9RhNBqI8VVEEswgU-0-3EVunJcsrhw9OBjTRIX9vrtfasvwYhE048LcIjZCJHc_NX8ek8iVCICsDiMpIFLLmyeTf230wygsQCm4l4Txwtg9xxqRmg_yQPwqS_Y21KPyOnwO92mhOsQTlTZ2sLSdNJtJ-WQFP5LkwQFUSs26ynT4NpfpDnRqTvrgSxMazHUcX01VjDWZwkAZaQ; __cf_bm=bF2mlVy0vLOuvGsXs2kNhTJFpZrYd6a9wR_astHLEgQ-1718735007-1.0.1.1-1GD41K.TROzZHn0SqUxf8Q_WJ3tek1GSUzHyt_TqppC0Q4BqwS7xaAay8mP1KnQuAIZ0vDxDE4akCk6mLkBiiA; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1718731564.174.1.1718735268.59.0.0"

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
