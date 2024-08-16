import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _gcl_au=1.1.40401959.1720444941; QSI_SI_d7sXai0ne02TH8i_intercept=true; _tt_enable_cookie=1; _ttp=YJJlcD_vXWEoZwbTE51InSddWyM; _gid=GA1.2.1064567622.1723640485; faire_mfa_suppression_secret=9goxzeykvrqcsnhszxlp727037vvt2g1yynyhhzagc; _cfuvid=nvu78orfR1pfFgDGfUgyn4GTl3GuXy_.0XqDJoAn13o-1723727551406-0.0.1.1-604800000; _ga_0D54RK9BRC=GS1.1.1723729454.1.1.1723729566.0.0.0; _ga_09CCX15SCN=GS1.1.1723729454.22.1.1723729566.0.0.0; _hjSession_3177092=eyJpZCI6IjU4NTlhNmFjLTE0MWItNGI3Yi04MDQ3LTVjZjliNDg3MjZmNSIsImMiOjE3MjM3MzAwNTEzMzAsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __cf_bm=IKbAzy7hlj40ywxLAS_hmnEunYfojWtqDR31WJbJFP8-1723731514-1.0.1.1-VPSZ81aHKcHNZhTC8O2PVmaR3ApVMV_oBiz6FJA_iMqv3G5Jaks.q40NZnh59mcNznXcMrGOoq0ZGr4fXv2EbA; cf_clearance=hG9wdHcTZY_JA_o_RDmZrb2ntolkHDbAPB3xTKL5XcY-1723731515-1.0.1.1-UKKzV3e4a.efjkn5PIpJjL6pOP8XCSMSMhlEvCH2H16Wnm6irwGePh.a69Q_Hq21dSw9XMErtt0fbgvcXRtprw; _hjSession_3000850=eyJpZCI6ImJlZTA2ZmU5LThmZDAtNDJmNC04NWQ3LWM3MzI1YjQwNTQyMSIsImMiOjE3MjM3MzE1NzY2NTksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _ga=GA1.2.1582770238.1704718676; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1723729454601.1723731581090.233; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiOTJ6cHhkcG9oZmhhaXdqNzNqaWJweXU5ejVxa2M4aTQ0cGtucW15cGg5Z3Vwa3cwZHdiNThwYW8zd3U4cnE5Z2x5a3lpeDlicDdmMnBxOHFnazJ3bW45am0ybnFrNjd4MWg5dCIsImQiOjE3MjM3MzE1OTgsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzIzNzMxNTc0ODMzLCJsIjoiZW4ifQ.vSyN-aJASjQYCD20k61Yjt2z5vLtXx2icMMBvdk-OKF0QQ7Bgq6LbhAxwYYL9rRfF0iYiRR7JoNKeNdQUY6CuK4Op-guyGgaqFkn-7oSKvRMTqMQJHzpL2yxoLAwBSVZSEpOic-Fxzb5T-EdMs_ykXZ2DXzzdwoDS00QBWg9kPDVur9T9xy_kuIKD1g2Be8RtDHWUS-gWbry1exDYMmWbP2qpBZwZv97s9gf1UW0HL22YOAzv4P6DYZgk68IzcRF8Lisfz9K-tS_Jk_h6g2BkrlnNfaoXbQSb7Y-CUWeKmSCMOID2ywGNXe0LrVnIG3TKIgN-QRj_IHKfaZdgisvWg; _hjHasCachedUserAttributes=true; _hjUserAttributesHash=157eb07a90e6c5c68fe05b140d8736c3; OptanonConsent=isGpcEnabled=0&datestamp=Thu+Aug+15+2024+11%3A20%3A04+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; __hssc=62287155.2.1723731581090; IR_21072=1723731604285%7C0%7C1723731604285%7C%7C; _uetsid=500608205a3d11efaee21383d497f206; _uetvid=d86963a0474811eeb792fb4adaaa7106; _ga_3FHCRNP43E=GS1.2.1723731580.231.1.1723731604.36.0.0; _derived_epik=dj0yJnU9Rjd4T3BScEJwdVY5Uk5Pb29rcm5nejdwZzBsMHUycTcmbj1sckk1dHdJdVRVOHppYWpUNlo0Ym93Jm09ZiZ0PUFBQUFBR2EtRHBRJnJtPWYmcnQ9QUFBQUFHYS1EcFEmc3A9Mg; _dd_s=rum=0&expire=1723732574948"

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
