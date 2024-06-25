import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _ga_09CCX15SCN=GS1.1.1718745312.21.0.1718745312.0.0.0; _ga=GA1.2.1582770238.1704718676; _cfuvid=QNrOktwrqYqJJGcrUmaqmyNu9hUgD1AmVol13GpLENM-1719234794857-0.0.1.1-604800000; _gid=GA1.2.519937840.1719249604; faire_mfa_suppression_secret=812jiy6v46hiyg4x8cfug2zl6c3zwa4i7efpg881yg; _hjSession_3000850=eyJpZCI6ImQyYTFmNjNjLTVhMDUtNDAyNi1iNDU2LWE3MDQ0NDRhNjJhZSIsImMiOjE3MTkyNjEyOTQxNTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __cf_bm=CwTZVn3GcOIN4d_PV0pDTV5TWNpWGPMTi_8pSPB7ihU-1719261295-1.0.1.1-IPW3IAdhc9qroOoVu7hNpSzZ2JaYSRwUMM1B2NGEyD2rNr9pC2.8C984kiSSzS2LCciS2QiMiwL2SGYU_8ySiA; _gat_UA-90386801-1=1; cf_clearance=HuJMZpiOFJuMjAT1Et1zmzAdDUu4LNczdHp_zUqfXxs-1719262082-1.0.1.1-NL6V3S9l3Crrc1IBSF.w4OEsr330Q9_aLRE1tVXR3S4Lpxesvw..GDaTrieuxIa.a_z82UE8Z0ck.a5g_8w7QA; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1719252401140.1719262088022.189; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiZW9vcXJpb3hmdXljdGt0dHlqM21seXJtazM4NTJ4eTh6b2x1c3dqenA2bWQ2anhhYm04NHdscW5iZ3VtZ2V3ZTV4M2FvaHk5Zm52MmFvM3djazlnc3kxc2FjZ3JsYXFscm5ubSIsImQiOjE3MTkyNjIwOTEsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzE5MjYyMDgxOTM1LCJsIjoiZW4ifQ.Y7sMJk-umyTUtSr7bEy81yVXHRD3vP0G8xpYZSi7sd2JXDCt9LFwkS97xek-0wtgYZzVN-8VUVKUAzIsUd2ekFsfRK6qS9AiaW3SIwitaRoi3skutL8lEiqs_FirO_3duhNArg1nZ3aCGo07eUQHmpKSbmjmBoAJUau_lkws4TPwr0ANfOksvaho_wbBwICazvYq4htHksBkt4wuv-5_EV6eND-XKFAfZRamd2xTU_7ygF4x1qEEALf5D3YkTGVl9ziF9JXC1dFU3e8-h4B5BNk7RpXMLKxNVSzVJLq_Ig_F78z6PyUo3RAF7c2IuK7iDvKuGUJUr5hX7hzzkBKRzg; _hjHasCachedUserAttributes=true; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jun+24+2024+17%3A48%3A16+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; _uetsid=fed6db50324d11ef8abf25b4670c13bf; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1719262096788%7C0%7C1719262096788%7C%7C; __hssc=62287155.2.1719262088022; _ga_3FHCRNP43E=GS1.2.1719261294.187.1.1719262096.43.0.0; _dd_s=rum=0&expire=1719262991994; _derived_epik=dj0yJnU9LXhNdDZJVmtabEo3czFVLV9waGtlQzZsUU1FY2hwSi0mbj1KaUNGeTFuMGZTYTNOUUJtc19VNm93Jm09ZiZ0PUFBQUFBR1o1MjVBJnJtPWYmcnQ9QUFBQUFHWjUyNUEmc3A9Mg"

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
