import requests 
import time

def cookie_token():
    return "cf_clearance=.DnEw9347pvs3EF0TN8VuHrdfbblUX5_hQ3Myh0FDio-1721225781-1.0.1.1-14oC.So5Iub6RyxNW5yWs9qj7Cqc7eiMR3.9EFrd4tQSjm40Unzz4pjoQlQZgXF6.zrPfj_BCAJL8FFnd_LsoQ; _cq_duid=1.1721225781.Him56LljJAal3kAe; _cq_suid=1.1721225781.TmBlXQ7apWTLjfUy; _fbp=fb.1.1721225781902.684203431790031284; _gcl_au=1.1.106802840.1721225782; _hjSession_3000850=eyJpZCI6IjQzMTc2OWQ4LWVjN2UtNGNkZS04NTAyLTNkODdlODk5NmY1ZCIsImMiOjE3MjEyMjU3ODIxMDAsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; _ga=GA1.2.258671140.1721225782; _gid=GA1.2.1873694082.1721225782; IR_gbd=faire.com; sa-user-id=s%253A0-fce61339-c75f-5e5b-5075-3e7e2b74eca5.qL1IfDCN0ZFL9XLzJzOt2oCcPosLYuKcOoKxG0UCbhE; sa-user-id-v2=s%253A_OYTOcdfXltQdT5-K3TspbUvBJE.rgxef5tf%252F0ywBSf07N%252F6t%252FjFbd4C4LElFiRFK9GoKgM; sa-user-id-v3=s%253AAQAKIM7WEQg_YDv5k95bv-Z3R4FQ4JCZHjqWSHsNISIIYxtZEAMYAyC2pN-0BjABOgQK5069QgThj6zN.2wUEZHbMvppNRrZlW5a%252BAfdo%252BsGKXanAd3jE%252FbcETMg; _pin_unauth=dWlkPU5XVTJOVE0wT0dRdFkyVmlOUzAwT0RZMExUbGtaVEl0TlRFNVpHSTVabVF6TTJRdw; __hstc=62287155.4185afc7afa493670b3ffbf826ad433c.1721225783298.1721225783298.1721225783298.1; hubspotutk=4185afc7afa493670b3ffbf826ad433c; __hssrc=1; localSession=true; _hjSessionUser_3000850=eyJpZCI6ImVmYjYwODFjLTgxYmEtNWRiYy04ZDE2LWUyYWI5YWVjNjgwOCIsImNyZWF0ZWQiOjE3MjEyMjU3ODIxMDAsImV4aXN0aW5nIjp0cnVlfQ==; _hjHasCachedUserAttributes=true; __cf_bm=KFXh4JVWPU_mrhVFNiRdP2nCTE4ueZwkM12ZwwYMQEU-1721226481-1.0.1.1-bwcN0C0SCq.HwZiwQulY.UUk.ctRlE6H_JBvt36l3TCFY40smiF1olDJVLXwjM.vQCWxRCD5esCcdAzLSpyC2Q; _cfuvid=0iPoZxDsLF2VrIbkNq09nw12jDceRQ0lETDAVBXr6vw-1721226481215-0.0.1.1-604800000; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Jul+17+2024+11%3A28%3A53+GMT-0300+(Argentina+Standard+Time)&version=6.17.0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&AwaitingReconsent=false; IR_21072=1721226534816%7C0%7C1721226534816%7C%7C; _uetsid=24ea1510444711ef90f535fd45c8ae26; _uetvid=24ea4d00444711ef943d7fc3996710cb; __hssc=62287155.12.1721225783298; indigofair_session=eyJhbGciOiJQUzI1NiIsInYiOjIsInR5cCI6IkpXVCJ9.eyJzIjoiNzlyNnVvenYxaWszMTl0ejN3cHljbGt4MmYxemd2eXI1enR5cmV2NGZ4M21jdmc4czlkZHp1ZTMwNnV2Z3BlcTY2aXcyb2pnM25mMnNtejJlc2Fzd205dmp0cngwYWcwaDUzMSIsImQiOjE3MjEyMjY3MTksImUiOltbInJfeWs2OGp2cTlnNSIsImF1X2E0OGVnZXNjOXQiLFsxLDIsMyw0XV1dLCJ1IjoidV9lYWdxaG13Y2ZlIiwiZiI6ImM2aGczNmRyaDV5MHZlbGlwYXRxOWhzNGo4bmRidzhoYm1xcXBpZjk4c3k5NHVoa2s4ZHNnZXRvaHA0eHdxcmZyemY0NXJlYjJndzJyaWhtbnk2c2Ezdm04bzk2cW5iZ24wNG8iLCJ2IjoxNzIxMjI1NzgwNjY4LCJsIjoiZW4ifQ.V-nzbY3DSK3zqqpTtL-aXNiFELXQdGBB6UR_vAMK0Ghhi47L54I9f8MgfSITa6utGtfD7ai89j5fy5RilRov9H_6wUOKbmqWLSlPuSBKWXGxaJKYhBg1AG8ysrPZb6nAMO_mMjBvv5eTNL2iSrLqdUK0qrBaZ2wrjp3zkkICgnr_E4yf7eAgi1qOtx987TRIgL5i8DNLRhIe2Y3QD85Oxuso48gmlLLK6hzxrLiMkF-cuk9ja2vOCadWOl5UqN4ykOXa0HsdQZwC1sB4CFS04z3giqzEib4aCXR55fgzEc7kVDp5PI8UiQRhUimjFG8BXno5oiBWpRpu6HfHvQODNQ; _dd_s=rum=0&expire=1721227806455; _gat_UA-90386801-1=1; _ga_3FHCRNP43E=GS1.2.1721225782.1.1.1721226906.60.0.0"

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
