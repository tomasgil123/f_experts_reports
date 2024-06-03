
import requests
import time
import pandas as pd

def get_customers_crm_page(page_number, brand_token, cookie):

    endpoint_url = f"https://www.faire.com/api/v3/crm/{brand_token}/get-customers"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    payload = {
        "pagination_data": {
            "page_number": page_number,
            "page_size": 30
        },
        "brand_customer_view_query": {
            "customer_tokens": [],
            "customer_filters": [
                {
                    "filters": [
                        {
                            "comparator": "EQUAL_TO",
                            "boolean_value": True,
                            "field": "ON_FAIRE",
                            "type": "BOOLEAN"
                        }
                    ],
                    "label": "ON_FAIRE"
                },
                {
                    "filters": [
                        {
                            "comparator": "GREATER_THAN",
                            "datetime_value": 1709262000000,
                            "field": "DATE_ADDED",
                            "type": "DATETIME"
                        },
                        {
                            "comparator": "LESS_THAN",
                            "datetime_value": 1716001200000,
                            "field": "DATE_ADDED",
                            "type": "DATETIME"
                        }
                    ],
                    "label": "DATE_ADDED"
                }
            ],
            "excluded_customer_tokens": [],
            "brand_crm_tag_tokens": []
        }
    }

    created_at = []
    email_address = []
    name = []
    on_faire = []
    source = []
    state = []
    store_name = []
    token = []
    type = []
    unsubscribed = []
    added_to_crm_at = []
    signed_up_at = []

    #v we try making a request 3 times
    retry_count = 0

    page_count = 1

    while retry_count < 3:
        try:
            response = requests.post(endpoint_url, headers=headers, json=payload)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                page_count = data["pagination_data"]["page_count"]

                customers = data['customers']

                # we iterate over customers and append the data to the lists
                for customer in customers:
                    added_to_crm_at.append(customer.get('added_to_crm_at'))
                    signed_up_at.append(customer.get('signed_up_at'))
                    
                    brand_customer = customer.get('brand_customer', {})
                    created_at.append(brand_customer.get('created_at'))
                    email_address.append(brand_customer.get('email_address'))
                    name.append(brand_customer.get('name'))
                    on_faire.append(brand_customer.get('on_faire'))
                    source.append(brand_customer.get('source'))
                    state.append(brand_customer.get('state'))
                    store_name.append(brand_customer.get('store_name'))
                    token.append(brand_customer.get('token'))
                    type.append(brand_customer.get('type'))
                    unsubscribed.append(brand_customer.get('unsubscribed'))
                break
            elif response.status_code == 429:
                    print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/3)")
                    time.sleep(30)  # Wait for 30 seconds before retrying
                    retry_count += 1
            else:
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    data = {
        "created_at": created_at,
        "email_address": email_address,
        "name": name,
        "on_faire": on_faire,
        "source": source,
        "state": state,
        "store_name": store_name,
        "token": token,
        "type": type,
        "unsubscribed": unsubscribed,
        "added_to_crm_at": added_to_crm_at,
        "signed_up_at": signed_up_at
    }
    return data, page_count


def get_customers(brand_token, cookie, page_number, brand_name):

    created_at = []
    email_address = []
    name = []
    on_faire = []
    source = []
    state = []
    store_name = []
    token = []
    type = []
    unsubscribed = []
    added_to_crm_at = []
    signed_up_at = []

    data, page_count = get_customers_crm_page(page_number, brand_token, cookie)

    # we wait fifteen seconds
    time.sleep(20)

    # we add data to arrays
    created_at.extend(data['created_at'])
    email_address.extend(data['email_address'])
    name.extend(data['name'])
    on_faire.extend(data['on_faire'])
    source.extend(data['source'])
    state.extend(data['state'])
    store_name.extend(data['store_name'])
    token.extend(data['token'])
    type.extend(data['type'])
    unsubscribed.extend(data['unsubscribed'])
    added_to_crm_at.extend(data['added_to_crm_at'])
    signed_up_at.extend(data['signed_up_at'])

    # we iterate over the pages
    while page_number < page_count:
        page_number += 1
        data, _ = get_customers_crm_page(page_number, brand_token, cookie)

        # we print a progress indicator
        print(f"Page {page_number}/{page_count}")

        created_at.extend(data['created_at'])
        email_address.extend(data['email_address'])
        name.extend(data['name'])
        on_faire.extend(data['on_faire'])
        source.extend(data['source'])
        state.extend(data['state'])
        store_name.extend(data['store_name'])
        token.extend(data['token'])
        type.extend(data['type'])
        unsubscribed.extend(data['unsubscribed'])
        added_to_crm_at.extend(data['added_to_crm_at'])
        signed_up_at.extend(data['signed_up_at'])

        # we wait fifteen seconds
        time.sleep(20)

        # every ten pages we download data in the arrays to a csv
        if page_number % 10 == 0:
            partial_data = {
                "created_at": created_at,
                "email_address": email_address,
                "name": name,
                "on_faire": on_faire,
                "source": source,
                "state": state,
                "store_name": store_name,
                "token": token,
                "type": type,
                "unsubscribed": unsubscribed,
                "added_to_crm_at": added_to_crm_at,
                "signed_up_at": signed_up_at
            }
            df_customers = pd.DataFrame(partial_data)
            # we download dataframe to a csv
            df_customers.to_csv(f"customer_data_page_{page_number}_{brand_name}.csv", index=False)
    
    data = {
        "created_at": created_at,
        "email_address": email_address,
        "name": name,
        "on_faire": on_faire,
        "source": source,
        "state": state,
        "store_name": store_name,
        "token": token,
        "type": type,
        "unsubscribed": unsubscribed,
        "added_to_crm_at": added_to_crm_at,
        "signed_up_at": signed_up_at
    }
    df_customers_final = pd.DataFrame(data)
    # we download dataframe to csv 
    df_customers_final.to_csv(f"customer_data_{brand_name}.csv", index=False)