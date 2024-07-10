import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _ga_09CCX15SCN=GS1.1.1718745312.21.0.1718745312.0.0.0; _ga=GA1.2.1582770238.1704718676; _gcl_au=1.1.40401959.1720444941; _gid=GA1.2.22357527.1720444942; _cfuvid=.1oSU_bj.AopLDfyyu3U49IhONpTUVgUHTxjXL_abFY-1720540418950-0.0.1.1-604800000; faire_mfa_suppression_secret=ae8skpshctj3p744trambdplle172rvyw8n7o6qwak; _hjSession_3177092=eyJpZCI6ImNmNGI4ZmFmLTA3MDgtNDRlYy1hMmMyLTE5ZmNkODkxMjhkOSIsImMiOjE3MjA2MTg4MTA3ODksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; cf_clearance=CDuJVC9oxq._xu2rxeZ.h07iui_ekHOlOKr8YHORv0Q-1720619620-1.0.1.1-bijlMPqMSH.cezlZrbDEkMbQ95fQnx7Jno2h5RNR28RQZg7wcZWmJnQOvEl_H._La25hBRFeccm.YNgzwgDnNg; _hjSession_3000850=eyJpZCI6ImM4NDZmMzQ5LWQ5NTctNDg0Yy04NWNmLWViZDc5MGVmYTNjMSIsImMiOjE3MjA2MTk2MjE3MzAsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1720543686500.1720619627099.209; _hjHasCachedUserAttributes=true; _hjUserAttributesHash=157eb07a90e6c5c68fe05b140d8736c3; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jul+10+2024+10%3A58%3A35+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; _uetsid=1ba113803d2d11ef8ab3dbc4899609fc; _uetvid=d86963a0474811eeb792fb4adaaa7106; __hssc=62287155.16.1720619627099; IR_21072=1720619915922%7C0%7C1720619915922%7C%7C; _derived_epik=dj0yJnU9RUJ3ZDlTX1FKVDRfWmNvejkxMVBKVlFLT3JXNDA2V0Ymbj1EM2x2XzdXNlVRTWhkOGE5bjNscEVBJm09ZiZ0PUFBQUFBR2FPazR3JnJtPWYmcnQ9QUFBQUFHYU9rNHcmc3A9Mg; __cf_bm=GvhoKLEP83cNW4911aT5z2rIJLuo.d8pqnTDZJkv4Vc-1720620540-1.0.1.1-3IKt6GozDVcv0P3oCqmbNEa49yo_GLq4FUAU4HZTKNHnmRpr.O3eorHmivzYoGsbFAAhic.q.Rbkp4RJZl.neQ; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiZHAybWF1YW10NzlxOWpydzg0Mjc5YWtlZjI3YTdjOXk0azd3OXl0cnhqMGVyYXBjY2wycjB0eWpheDFkOHg1bXBvanUxb2R5eXRrN29uNjV3ZHl3ZG93aGt4bnRzZGFxM3pmbyIsImQiOjE3MjA2MjExNjksImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzIwNjE5NjE5ODg3LCJsIjoiZW4ifQ.oFqmYK97gDpXhhNIKf36ILw1R8udpbZemgLcHFOrzRfwMQDp3bVtrN_1iUDpJNFk5z1bt3ojm4fC-5U-4Z7eaeShCTg0RWvFgSgnVRIGUQ8xeqQC6BLplZwhQAQjhgSzJDiYtUdQ9UDjU02dxgTcIgYWxFjk0N2u_3kw1L6Q7-YI7fXdBsQlqmd13HipSKjqK1zKnz1s8jwPZfB4vr8Bp-xFwTbllNYLcDXxYMH2kEenPT1o6a7QMJwquTE_ju8fnqe5FzUOG122rHxuZlwIxsauFJcun9tgOSeqqrNZOTAtxUjbcZHZBQfpEIZWQf0Xg3PJ8jPmt2InH9dmZeSgiw; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1720619626.207.1.1720621181.60.0.0; _dd_s=rum=0&expire=1720622082066"

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
