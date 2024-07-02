import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _ga_09CCX15SCN=GS1.1.1718745312.21.0.1718745312.0.0.0; _ga=GA1.2.1582770238.1704718676; _cfuvid=QNrOktwrqYqJJGcrUmaqmyNu9hUgD1AmVol13GpLENM-1719234794857-0.0.1.1-604800000; faire_mfa_suppression_secret=812jiy6v46hiyg4x8cfug2zl6c3zwa4i7efpg881yg; cf_clearance=E.YaZFiA.HumfZScnHlkVnXDBRHsnv0lqMIlOTvmdWk-1719607518-1.0.1.1-EbrwjpOTaAPPA_F6aNTvNAZEnVkllbQo1L.vIT8OC6DOBZs.VRproE1w3YKFQ85eyyhgwhzTPAJoCGL2ZLfDuw; _hjSession_3000850=eyJpZCI6IjA3NDZiYzA2LTQ3NjctNDZmYy05Yzg3LWYxN2ZhZjVhNGNiYyIsImMiOjE3MTk2MDc1MjgzMzcsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.124456526.1719607533; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1719492722821.1719607533583.198; _hjHasCachedUserAttributes=true; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jun+28+2024+17%3A57%3A51+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; _uetsid=5d2419d0358f11efa8fe253f5ce1aef1; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1719608271579%7C0%7C1719608271579%7C%7C; _derived_epik=dj0yJnU9V3ByYjdhakFZQ2hUUnZLRzN0c1hoWVRMY19hOTB2Wlcmbj02YUxPV2s2czRYUjAxdl8ya2E5TFNnJm09ZiZ0PUFBQUFBR1pfSTg4JnJtPWYmcnQ9QUFBQUFHWl9JODgmc3A9NQ; __hssc=62287155.5.1719607533583; __cf_bm=AU0L4IdNq0DPC9dTkBZMK_k8Sk_hcRNqj5Q4wY_LwYs-1719609338-1.0.1.1-JqqupX7YaU9vWwYDIcK_x1ZoXO48C26pzg2OT7yqhZNVs8rmyArc22Q5c5p2gRCqzLyWFAR7rkbxcZKe5UD2lQ; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoia29tNDNiNGg4bHI5aWl2cGxoY21vc2xyYXNrNDk0dTE2eWVwcm5qZzA5Z2Y0bHcwODNreTlrMGdhbm5tMXpnYW1wamR5ZXZzcTFlOGNmMTRkbjNuZnJ4bTB6dGlqY2g0YTc0ZSIsImQiOjE3MTk2MDkzNDAsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzE5NjA3NTI3Mjk0LCJsIjoiZW4ifQ.jV6ihtYzwq-_6ESwcQumGPEMASLvEMXLZDsUNKq4IJ4PbiFhDTCVxdyWYzOMZ06UZbjWaGa2Wdu9uSMb3YEeIVEaiN-qJuu7mrx63KmjanfDmt_SwuYrrMgvyM3X2luZlKCibWFqMGc6sAszPjZOTzrge5Ej5KUpDeM25BhjDv96WLsfrQ3M-EHGi-UeXh7OTyq5qqVcEyVvjg-bbuk2fM4ZRm7rT_iCkhCX3mPbRzpGqzEcV4NtX0oOSyapTEvpKqUE8pGKmX7ABnDyHKTf3-PL32-v7a0LkUQRH7vSIQK-1X9b4vTj4bDWevmJnVFIOnNmgCM_88aqaREQY-ICww; _gat_UA-90386801-1=1; _dd_s=rum=0&expire=1719610493818; _ga_3FHCRNP43E=GS1.2.1719607533.196.1.1719609594.59.0.0"

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
