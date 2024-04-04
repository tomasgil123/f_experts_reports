import requests 
import time

def cookie_token():
    return "_gcl_au=1.1.1544957958.1704718676; IR_gbd=faire.com; _pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; __hssrc=1; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; faire_mfa_suppression_secret=b200dwf6tixlfnzzyz9wa4z1cbnq5u4svmsn40woe0; _fbp=fb.1.1709731797476.527673433; _ga=GA1.2.1582770238.1704718676; _ga_09CCX15SCN=GS1.1.1710366989.14.1.1710367004.0.0.0; _gid=GA1.2.2057852643.1712063474; _cfuvid=J9Sg_B3oS8y4ZHRSZhBI7ejoMimEEQQ_Nyjap2_.HMA-1712149299365-0.0.1.1-604800000; _hjSession_3000850=eyJpZCI6ImIzOGZhYjBmLTU3MDctNDAyNC04MjdkLTI1NThhN2Y3ZTU3ZSIsImMiOjE3MTIxNjA4MzcyMjksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; _hjHasCachedUserAttributes=true; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1712152978924.1712160880206.88; _hjUserAttributesHash=036847d7968040fe83b960808e9d8614; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Apr+03+2024+14%3A38%3A22+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _uetsid=7b9825d0f0f211ee92893510a61d303a; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1712165902515%7C0%7C1712165902515%7C%7C; _derived_epik=dj0yJnU9R2VqMXJSZkQxbXBhTTd5aDJDemhxUFZSaVNVcWF0bGMmbj1KSmhrTGFCU1ZBeEw3T2VvaDdOQ29RJm09MSZ0PUFBQUFBR1lObEE0JnJtPTEmcnQ9QUFBQUFHWU5sQTQmc3A9Mg; __hssc=62287155.16.1712160880206; __cf_bm=Kx4d2nahK4.dYbRP9Od8v1ZXTC9KVbHAGhc781jT9pc-1712166700-1.0.1.1-qpagHr3ihie1vwsRyRE9hJDkhQdjgCYg_lZZKL2_TB4EtT.nYP2lgHWRls11CdKHcb4pWMkUMF4upJq_VZGKyw; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjEsInR5cCI6IkpXVCJ9.eyJzIjoieThyemkxa2ltazByc2p3ZGNkZ2dnMDZ4YzZrYnA2dmN3MnVlZ3QxejRndXNiNHdtZjRyM240c3JpcjZ5ZDl2Y25vOWtyOGlpd2R6bTk1d3JhOWhvMnRnNXI2MGtyZjBsYXg3dSIsImQiOjE3MTIxNjY3NDcsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiXV0sInUiOiJ1X2VhZ3FobXdjZmUiLCJmIjoiYzZoZzM2ZHJoNXkwdmVsaXBhdHE5aHM0ajhuZGJ3OGhibXFxcGlmOThzeTk0dWhrazhkc2dldG9ocDR4d3FyZnJ6ZjQ1cmViMmd3MnJpaG1ueTZzYTN2bThvOTZxbmJnbjA0byIsInYiOjE3MTIxNTI5NjIsImwiOiJlbiJ9.Nw1PQwa2CyK4nyHf7lRyollDz1yPnuigsJP_o_NaU_ra96vrOa9BJFf0CdFrlkwkjoJTPlHkqi7sBKyvj3TCWbQeHitni49rRJfDp6MjdSNnHD3_gRzHJTL6B9R6lAzMbXy27ZvR8N0pDPHDbUlUhCTf9UyLrqCtA-FJbraiRlsbv4T37aaG6JqOF56r1rB96Bj29kuKtcSlBuO3OpE5A3ZO-8df588HzYMoQ0T7X0Y1O7Tqjx8iVFDUCceFgBx8q4Fev78Hj1PdNRILfqC18z4JdvtawkzFWLG529vqBqhqlwj4tF8y_lNIq7eXhwmFI6q27wyBnGypBq4w348WPA; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1712160836.92.1.1712166777.60.0.0; _dd_s=rum=2&id=71801e64-60bb-431f-8b51-67fb6553bb19&created=1712163846010&expire=1712167689521"

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
