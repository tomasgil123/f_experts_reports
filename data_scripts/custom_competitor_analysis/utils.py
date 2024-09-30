import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _tt_enable_cookie=1; _ttp=YJJlcD_vXWEoZwbTE51InSddWyM; _ga=GA1.2.1582770238.1704718676; _ga_09CCX15SCN=GS1.1.1727110279.26.1.1727111237.0.0.0; _ga_0D54RK9BRC=GS1.1.1727110279.5.1.1727111237.0.0.0; _gcl_au=1.1.40401959.1720444941.935955205.1727349122.1727349160; _cfuvid=QuUcV_ArmtXddSii97qegmQNLq6A_p4xjOOc2RYJX18-1727715201086-0.0.1.1-604800000; __cf_bm=nydAfSqSV2LV0Lf5B4SkJJlPjvI15erfOVbfi35vqmg-1727718653-1.0.1.1-0iw3ShLKWfhZHBGz9aEFdjJtaDgD8S67TJ3uh6xtyRAuaUCQT0p7YncWxaSrIn9g3hRmVY8WivGnL1nWzAX0xg; cf_clearance=KL.t7q9IxF.eW3w_y7MMDnE8L0pmLc1zi5I.yh9Hbs0-1727718655-1.2.1.1-UsnmLrhmemcOSRafXmnjSGOAoav5dlQGc109Ts3V9URNBX5t7QU68K4qEH7jnYp7mb8NXWSIDDm4ggY.GxJAna_k0Boabn_0Gz_88DIC7gG.ZNe88SYrOzHDe1wouyxuvNTojCk_JUqSVAGZ3ShYVvj1Y6Ms34nWw7KTPghA3OI_jL1OFec0gtW8JiT7hRmUDlcbxZcndKxitzqTSaD5uWg32uSbs4Mk759qg75kt4ODED5VT5zyoQLdmhGK1Tb7nMQPNUlOIKgJPmdwZtNVB_o39SnEnZ0lrnrA7Sso9AwPZafpgfgunxhiioNOf_XHiVKaDGmCLnZB_V7smeyR487TiqqMvNq4r4BVOExs7hL_L.klweGO0GpMvWA5j.gSYvZO4eWoEpFvJg3IcSR5rA; _hjSession_3177092=eyJpZCI6IjE5MTU5NDBjLTU2ZWEtNGMzNy05NWQ1LTc4ZDE4NmZkNTNiNyIsImMiOjE3Mjc3MTg2NTU1NjAsInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjUserAttributesHash=0812f3acbabacf0a1cb4da3a0266e4e5; _hjSession_3000850=eyJpZCI6IjVmZjAwMjllLTMxZDktNDJlMi04OGRjLTQ0YzhkYzlhMTRkNiIsImMiOjE3Mjc3MTg2NjUyMTUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _gid=GA1.2.2144819188.1727718670; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1727349078774.1727718670050.260; _hjHasCachedUserAttributes=true; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Sep+30+2024+14%3A53%3A56+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; IR_21072=1727718836537%7C0%7C1727718836537%7C%7C; _uetsid=938276507f5411efb9f113c4eeba8dca; _uetvid=d86963a0474811eeb792fb4adaaa7106; _derived_epik=dj0yJnU9NV9TWllYVWpuNmtFMUZrMWIwVDVHeVdmWVNtenhDc3Ambj1YVnB3Vkt1alp2cFRoWEh1VUNNSmNBJm09NyZ0PUFBQUFBR2I2NWJRJnJtPWYmcnQ9QUFBQUFHYjFRWHMmc3A9Mg; __hssc=62287155.12.1727718670050; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiOGswd2tjdTF3ZHdiOTg0azU2b3V4a3ZxaDV2amVkdWw2dWZxcnR1OHZveGdxeXFlODJhMzlydDIyMmw3c2s1ajhkeG54Mjg3OXViMmZ4eWhucm5jNzAxY2RuNjAxZ2c5YzJ2eCIsImQiOjE3Mjc3MTkzMDksImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzI3NzE4NjY0MDc2LCJsIjoiZW4ifQ.dlI6c-zgOrKP6rHPyhlBuGnoTiRc2g9mkEkinarh08uUdyDSK7YwWK0tzROwdBreT1yvUggL4pV61tJ0MuVOaFP1U4wzyZwLj4FG9f1B7i1GLr77XJr44Y5pBvhpkic89s9i75K6EinaiVuBt8xVRgiSabcLBzdkqpj8ZXx7f3jKyKrFYy4qY-KvQM7lo86rkB2GuO6d7V5ZhsfPgoyylTI2ogr7tIsK0MVu0FDgSBYusF6XChF1oBnofdOlUfmLx-4seOq9hOLRqYXS3hSbbOkE8cviQkU1PSGPrqcVrAufjhVCIS9RKPCqOFa4xbsWjPPf67pKrbBZjDBclZkS_w; _dd_s=rum=0&expire=1727720224567; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1727718669.258.1.1727719324.60.0.0"

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
