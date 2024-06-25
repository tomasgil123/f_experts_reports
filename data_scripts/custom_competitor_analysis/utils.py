import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; X-IF-OVERRIDE-LOCALE=en-US; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; localSession=true; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; OptanonAlertBoxClosed=2024-05-24T16:29:59.048Z; _ga_09CCX15SCN=GS1.1.1718745312.21.0.1718745312.0.0.0; _ga=GA1.2.1582770238.1704718676; _cfuvid=QNrOktwrqYqJJGcrUmaqmyNu9hUgD1AmVol13GpLENM-1719234794857-0.0.1.1-604800000; _gid=GA1.2.519937840.1719249604; faire_mfa_suppression_secret=812jiy6v46hiyg4x8cfug2zl6c3zwa4i7efpg881yg; _hjHasCachedUserAttributes=true; _hjSession_3000850=eyJpZCI6IjE3ZjAwM2VmLWJmYTctNDA2Yi04YzlmLWJkMzYyZWVkYmU3NyIsImMiOjE3MTkyNzc4MzcyMzYsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; cf_clearance=AbX75uZlojYSrkbCAbWJ.nHTOzLi2hVSmdjsnBEd46Q-1719277922-1.0.1.1-ww7j1qt3iZVoWFfqOlNHu9p8LZu1DjR9B6MaJEKG1wR6IXTFtdE0kxvlmMnnUlafunRJqEZlLHyl.3W08kzFBg; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1719262088022.1719277927972.190; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Jun+24+2024+22%3A12%3A54+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=AU%3BNSW; _uetsid=fed6db50324d11ef8abf25b4670c13bf; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1719277974888%7C0%7C1719277974888%7C%7C; __hssc=62287155.6.1719277927972; _derived_epik=dj0yJnU9a2V3LXBkMm1HMWJ0YkVGZXJ4NC1tNzkzVXRMTTlJQ2Imbj1WTk1HQzNVcGlEX1lwRm5EalRCYkVRJm09ZiZ0PUFBQUFBR1o2R1pjJnJtPWYmcnQ9QUFBQUFHWjZHWmMmc3A9NQ; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiZW9vcXJpb3hmdXljdGt0dHlqM21seXJtazM4NTJ4eTh6b2x1c3dqenA2bWQ2anhhYm04NHdscW5iZ3VtZ2V3ZTV4M2FvaHk5Zm52MmFvM3djazlnc3kxc2FjZ3JsYXFscm5ubSIsImQiOjE3MTkyNzkxNDMsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzE5MjcxNzAzMzc0LCJsIjoiZW4ifQ.vRsCYKQ2MCRMJuxWTFbP9lq-mW3K9e7-GFRAs5q-T9zoBunPVKvu6U2iXbHqJl4o2q8jhDP7RzIQ8WpIFoZIUzCVZ4OGTA1SDvf9zfQJlhP0SCXlv91Y108ppBq4hSCTEaOS38kqWxE-OEob0XXwDz1IXkCqjuFhE1JloucTg3Z73H2OoYB_7wgwkL-Fenup4lZb5wBxmgG8Xzy1tvqvhOG0TppQs08ceH9ejHlj3JSDYfeYs-_7AMj--4CQ6fHaLxUR3faLu-yAjrsDAhRgDaLeE2bSyFyy2JDMF2Kvb9ztOofu6wrxDWZHp15kTZpsl2uwQT_xuZeDSDR9Q6shJQ; __cf_bm=FyUM3BH9fOCyWdol2J9B.zZ_CCIWal7j5GSkOfvvL1U-1719279203-1.0.1.1-ibnQnCVswrjQhgMeXsax_VE2QBTuJhDDXM0aPzFz8s_h8irdjIU5bqAD865pM6QpaTit4xpx_LzrQuKD1FBGJQ; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1719277837.188.1.1719279312.59.0.0; _dd_s=rum=2&id=fa7cf3e6-d8d6-4761-9077-7b32a61db7ad&created=1719279186399&expire=1719280211992"

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
