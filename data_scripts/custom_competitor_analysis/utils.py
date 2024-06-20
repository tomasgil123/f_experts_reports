import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _cfuvid=xB0NYVVvwCOlKj1pqDPdIVPbXXYd_DykKVPcc_xvzE0-1718465296721-0.0.1.1-604800000; _gid=GA1.2.1931496025.1718576362; faire_mfa_suppression_secret=4golr5xw9niid20t5y92o0r9rdfl87qgigvbcc50tj; _ga_09CCX15SCN=GS1.1.1718745312.21.0.1718745312.0.0.0; _ga=GA1.2.1582770238.1704718676; _hjSession_3000850=eyJpZCI6ImNlY2Q4Y2MzLTQxOTItNDIwYS04MzNhLTYzOWNjNDFhMTk4OCIsImMiOjE3MTg4NDI4NzEwNzEsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjHasCachedUserAttributes=true; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1718832551013.1718842887491.183; cf_clearance=b5fQ7CK3H_0cFRd9RgCCdYeBPBTGYezf.JrknHqeLOA-1718844871-1.0.1.1-tyRUIOEhX5hX89FUNJwH9lBv3HmhSPoC1ST0zBn4WYb4AZoA9sZK1JdEpnuYjB48FzuoMQLDfL82GC.zykIsQQ; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jun+19+2024+21%3A55%3A20+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; _uetsid=70ce4f202d7611ef9bacab490a79c606; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1718844920725%7C0%7C1718844920725%7C%7C; __hssc=62287155.12.1718842887491; _derived_epik=dj0yJnU9WFV4NEJfdWxhQV90YmU3RmM5U0JHaGNuQmJ5UmZtMzImbj1EWnlnX3pERzM0V0tsZnctcnVQTGFnJm09ZiZ0PUFBQUFBR1p6ZmZrJnJtPWYmcnQ9QUFBQUFHWnpmZmsmc3A9NQ; _ga_3FHCRNP43E=GS1.2.1718842870.180.1.1718845024.7.0.0; __cf_bm=oqp919NSlHM1zK8aBokVivT1rqQ4fHM.Sijj7Xaoz1U-1718845085-1.0.1.1-KeEbBIbJb8NprteF.9mRLik604tLAuH_yRVcLAqoJwcOmsVNdth5VwLvVoJ8ig3iouds7Ow4PmcI3T890279CA; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiN2Y2cHB5dGFjYjYwZnJsNTY5aHlmNHJveDc0bGhkbndiNTh4azVpZzZqOWhmYjZtNDhlOGgwcWJpcmh6YnA2cm0xMWdreDhsejFiaDNyYjJ3N29ydzRrMzlydWY0dDByNm1iZSIsImQiOjE3MTg4NDUzODUsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzE4ODMyNTQzLCJsIjoiZW4ifQ.kJabCC5t67xXa7nqDlb8g3qCIb0mwwEr2PkIm0mozUqwB1-zq5RRhOE6O-7iC8a_tpDsg1rpZmBkbi__HDutVAYzD7CmXQxTEl3NxDn7GD-pC-rfFJ2sF-1yzYvbqOq4WiaOlR0Ly9FtIpjnWd9W7a_ByEiKNwYYoAMB2QkNJKPV0I9keUsVx6-M_akjNvmn3Ics1jBoxS10HBl6yNC0J3cUiIeaFBuT6uvmvxg87dOhApGJ07s9if4Zr052h-l-Xrd0FoWVW_owshyqynTkpPtNNn5BOG-rh8K0aHFsFd892QxqjedADnkYdO-Ii7d1VN14uCnlqVJF9FXsW17nnw; _dd_s=rum=0&expire=1718846565343"

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
