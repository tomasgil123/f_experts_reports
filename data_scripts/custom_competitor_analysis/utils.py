import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _fbp=fb.1.1709731797476.527673433; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; _ga=GA1.2.1582770238.1704718676; _ga_09CCX15SCN=GS1.1.1713883291.16.1.1713883449.0.0.0; _cfuvid=HRJg1IYlxIVhEqngyprnh3ZHLoFfvbdJZhe43qOujQ8-1716226021651-0.0.1.1-604800000; _gid=GA1.2.1462736104.1716226028; faire_mfa_suppression_secret=1w8zry4ac2o72g5fjpmoa5ihz28d83kiyzldb29pzv; _hjSession_3177092=eyJpZCI6IjE1ZGNmZjFkLTcwODItNGFmMy1hMzU0LWMzMjM0ODBjODMwOSIsImMiOjE3MTYyNDYxNDkyNTEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; _hjSession_3000850=eyJpZCI6ImM1MjJkMjA0LTIzMTAtNDllZC05Yzc4LTBjYTI1Njg5NWJhOCIsImMiOjE3MTYyNDgxODA4MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1716226028771.1716248186196.141; _hjHasCachedUserAttributes=true; OptanonConsent=isGpcEnabled=0&datestamp=Mon+May+20+2024+20%3A40%3A51+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; _uetsid=2eeb823016ce11ef945c955b2fb6a5ce; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1716248451483%7C0%7C1716248451483%7C%7C; _derived_epik=dj0yJnU9OEtlcGZmUXpDaFdwZHVNZVVvSFYwTHlHY3dJRERVeUkmbj10U3ZudnJBbC16bmx1UkdXdjJOOE13Jm09ZiZ0PUFBQUFBR1pMMzRNJnJtPWYmcnQ9QUFBQUFHWkwzNE0mc3A9Mg; __hssc=62287155.12.1716248186196; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjEsInR5cCI6IkpXVCJ9.eyJzIjoiMjkyNmluZ2dwZ2p2YndiMm5jNm56aWgxZDMxMzBiZ3p3cDd5OXd6bHM1NjE1emdoYzdlMWI0eWpzbWg2enE3aGNxYnY0Mjk4NjRwZGVyeWFkdWtmcnJlbWozdXFrbTBsNWdsdyIsImQiOjE3MTYyNDkxMTYsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiXV0sInUiOiJ1X2VhZ3FobXdjZmUiLCJmIjoiYzZoZzM2ZHJoNXkwdmVsaXBhdHE5aHM0ajhuZGJ3OGhibXFxcGlmOThzeTk0dWhrazhkc2dldG9ocDR4d3FyZnJ6ZjQ1cmViMmd3MnJpaG1ueTZzYTN2bThvOTZxbmJnbjA0byIsInYiOjE3MTYyNDgxNzUsImwiOiJlbiJ9.h83XhRTqX9CEkZEgRAw6b0N5Mti56ZUCrGPrn9qb45bZR6gTZ63izs_3ADmVpPhBzKatNl4QqhYCUx6bZxfdU9zX4gm5ZCHRo72x3vXGad_7Eh7XkimMHDEr-Sp5-OTQ3FOrkYsfuVWNbtd4EmkTJD_KYiQtOoMAAx2MFfWHsf6bJUZS7BVWj7eCAJYq4pr2Mvqh6Cvt-ktF274-0bEugTuC43oFE6gJTjUvU0tjV-bb7KhLTfB_F1l3chx8_w_ISmiZv7SqzumKWdSlsqPMCd0p4Phz4FqJe-J8FEEw3n7n4RUJFJtbbtTvJclKkUbOQsWH-WcBPbPZxOfFuN_HLw; __cf_bm=r94IDbj6PWLxBbxb666daykB0TUDkma7DawEWt7E3Bg-1716249116-1.0.1.1-vaRJxnj3MfXs0rEwLmAz4UF1PQ6iHq9WQbTvUXaa4o8YQM3pIYZHdrUKWeXURrVyk17OuWnvTAuxOPlOGJ4Z1Q; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1716248185.140.1.1716249171.60.0.0; _dd_s=rum=0&expire=1716250071463"

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
