import requests 
import time

def cookie_token():
    return "_gcl_au=1.1.1544957958.1704718676; IR_gbd=faire.com; _pin_unauth=dWlkPVpEQmpNemN5TURNdE16Z3lZUzAwT0RCbExUa3hOR1F0TlRJNE9UazFZV0UyT0RJMg; hubspotutk=007a3e2fb136a02c1469dbec1fbb3387; __hssrc=1; _hjSessionUser_3000850=eyJpZCI6IjhlNGZmN2UwLTQ1ZmItNTQ3OC1iOTQ1LThiYjJiMTEzMzNkMSIsImNyZWF0ZWQiOjE3MDQ3MTg2NzIyOTksImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3231906=eyJpZCI6Ijc2MGFiMjJkLWQ2YjctNTY3NS1iMjg4LTM2YmM1MTc4ZmQwNyIsImNyZWF0ZWQiOjE3MDQ4OTg2OTQyNjIsImV4aXN0aW5nIjp0cnVlfQ==; _hjSessionUser_3177092=eyJpZCI6IjFjMGY1NDlmLWIwOWEtNWI5My04N2I5LTBkNmZhNmJhOTVkOCIsImNyZWF0ZWQiOjE3MDUwOTY2NjUwMTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga_7JY7T788PK=GS1.1.1707441754.3.0.1707441754.0.0.0; faire_mfa_suppression_secret=b200dwf6tixlfnzzyz9wa4z1cbnq5u4svmsn40woe0; _fbp=fb.1.1709731797476.527673433; _ga=GA1.2.1582770238.1704718676; _ga_09CCX15SCN=GS1.1.1710366989.14.1.1710367004.0.0.0; _cfuvid=SVA.58wN_W5DgDMarpSehaUcBJ84uJD.BXf2wlP9Ido-1710507556293-0.0.1.1-604800000; _gid=GA1.2.14409418.1710508510; __hstc=62287155.007a3e2fb136a02c1469dbec1fbb3387.1704718677049.1710512200456.1710528129364.72; _uetsid=0d0c68d0e2ce11ee861d1b5996c615e1; _uetvid=d86963a0474811eeb792fb4adaaa7106; _derived_epik=dj0yJnU9U3g0Z0dCQVpIWDZ4Q05GWEF5VGkyQkZFMzhvX1dCM0ombj1UMjdhLWtZejZ6c25GSjM4U2JhTkdnJm09MSZ0PUFBQUFBR1gwbkZnJnJtPTEmcnQ9QUFBQUFHWDBuRmcmc3A9NQ; IR_21072=1710529624698%7C0%7C1710529624698%7C%7C; __cf_bm=z8w0QV6CMsCDLkzGrBjbdRNEI5zUIKEIvx0p5B_ETv4-1710541315-1.0.1.1-fHwrJ3prqqesg97iYwTQFxnfyHqp2L8zztyUOtXfZ1AW1fs38koi40mgxyxhaYGXWxLiZDCrKSdb_6dngu_Lbg; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjEsInR5cCI6IkpXVCJ9.eyJzIjoiMmRrajFoMmU0bzloYzZ5YWNmbXJobGlvbDE0dDl4d3VyMzdmamFzbXB3Y2hhNzBrYXIyYWdydDl2dHF1MDBpYnVjbTJ5eW9nb2k1NDM2ZGtkN2RyMjkzZDM5bGIxNzMzeW1mZSIsImQiOjE3MTA1NDEzNzQsImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiXV0sInUiOiJ1X2VhZ3FobXdjZmUiLCJmIjoiYzZoZzM2ZHJoNXkwdmVsaXBhdHE5aHM0ajhuZGJ3OGhibXFxcGlmOThzeTk0dWhrazhkc2dldG9ocDR4d3FyZnJ6ZjQ1cmViMmd3MnJpaG1ueTZzYTN2bThvOTZxbmJnbjA0byIsInYiOjE3MTA1MDg1MDQsImwiOiJlbiJ9.GSXG_aSMo38wm6oCdZ8c_4SmDJY6RVtEcgfDmjiZ3030kzKvY42u50MZpZH5jGuBS8S28DRsEN2dpfvgRZHnMKvYbu_hDlLq0Ax_JR7wTpK2wJTya4-9b2p28TKYnf0g8DKgfWO8LQzfCTjgrrER1vyHqhhke-KJpVqUQmx2tUBxUpL2KLMQDKO3FQZT9CKNLVbfTOQvug_A0s4NiLvFfIcqecd5yFZC8dFXOhO6zDuYVVic9ZHcsdcpRi3P2zT8HjEk3LfTgoEj2baTJXj503W5tv0jEf4PZ92KQdga6-547a7ErHu_2k5riHXTnaQJ3fhLRU4B7ORRoBkFNsHYsA; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1710541577.75.0.1710541577.60.0.0; _hjSession_3000850=eyJpZCI6IjdlNGRiNTcyLTgzMmItNGY2NS05ZWFkLTY1N2Q1MzM2NGVmMyIsImMiOjE3MTA1NDE1Nzc2OTksInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0="

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
