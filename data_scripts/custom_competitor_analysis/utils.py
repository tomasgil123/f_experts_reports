import requests 
import time

def cookie_token():
    return "_pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; _fbp=fb.1.1709731797476.527673433; _gcl_au=1.1.1527690070.1712605646; IR_gbd=faire.com; __hssrc=1; _ga=GA1.2.1582770238.1704718676; _ga_09CCX15SCN=GS1.1.1713883291.16.1.1713883449.0.0.0; _cfuvid=ekJUfMGp5qX7tXUMLZVxlz8gsgBo9NtPoXVzO2eY3RI-1715608586968-0.0.1.1-604800000; _gid=GA1.2.1313711080.1715608593; faire_mfa_suppression_secret=bu30o6gzbw8n77s33y204zuzsahvv6qqn4dc0ig261; _hjSession_3000850=eyJpZCI6IjI4NWI2NDZmLWIyYTktNGM1Yy1hMTM2LTgwM2FiYjY5M2ViZiIsImMiOjE3MTU3ODA3MjI5NzEsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MX0=; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1715778218045.1715780730932.138; __cf_bm=g.GdLgqhANJAJkSumBha9IPcsprJ4C_PQVUxFwGIBdg-1715783329-1.0.1.1-t0rV.gPIXyKIZIxpHAGI2yV2zkXR1HgBSkImt1JVwq8QvdCk4ZGCqr7TF1nJ0RjG5SqNPu1qEAP57kURbpzRWw; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjEsInR5cCI6IkpXVCJ9.eyJzIjoiY2tpeDU4OXdib3M1cXBpZ2JzbHNvNWFrYThudzFrcmJqNDM3dzY2NXN4OWplbnVmbjY3ODVpdnlxZzVrdmJwN3ltYWprdXZ3bzg2NDRwN2p6YTFkN2kwcHY4cGRzMm5iN2J4byIsImQiOjE3MTU3ODQwMjIsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiXV0sInUiOiJ1X2VhZ3FobXdjZmUiLCJmIjoiYzZoZzM2ZHJoNXkwdmVsaXBhdHE5aHM0ajhuZGJ3OGhibXFxcGlmOThzeTk0dWhrazhkc2dldG9ocDR4d3FyZnJ6ZjQ1cmViMmd3MnJpaG1ueTZzYTN2bThvOTZxbmJnbjA0byIsInYiOjE3MTU3ODIyMjksImwiOiJlbiJ9.jos13CTDnX0t6m0p393bmcxlB_eaSHhwE9FcRw-rEWZGpSOxmGSdmDqhu1hnGY7wimgNQExZndzcD-yMX69dHG32gG8zskNXZbYQyGtriB_J-OU-AYhotvpkhrOjzI3lHJGDy0N5D_8FExOj31NwbZWVTajayBO23aIV-_E6yM9n3na2B8u5UrWgnHJXAuevEj6wy0DXtgdNGF3SxlZJquKooqNTbCP-xjBekZx3bN2uO0ZhqFNV1_Dgj1ZysomIrwHcXw0SB2L_4jePY54tpUSD2S2FtrtULY3E8Yemhut--DSu0XjTUiJQJaZnCJqhYicb4R3slFNrMPAaEIhKzA; _uetsid=9b141770113011efa7578b267b71c538; _uetvid=d86963a0474811eeb792fb4adaaa7106; IR_21072=1715784028369%7C0%7C1715784028369%7C%7C; __hssc=62287155.9.1715780730932; _derived_epik=dj0yJnU9azA4U3FfMXFXNWFrZ1NqZGZXT2dsbzdZVW1YTjNYX0gmbj1faWJmSkFDS3VDTF9hQ1FUQkxlR1p3Jm09ZiZ0PUFBQUFBR1pFeVZ3JnJtPWYmcnQ9QUFBQUFHWkV5Vncmc3A9Mg; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1715780730.136.1.1715784093.60.0.0"

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
