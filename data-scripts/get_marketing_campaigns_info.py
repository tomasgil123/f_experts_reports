import requests
import time
import json

def get_marketing_campaigns_info_page(page_number, brand_token, cookie):
    
    endpoint = f"https://www.faire.com/api/crm/brands/{brand_token}/marketing-campaigns?calculateStats=true&page={page_number}&pageSize=20&type=ONE_TIME&sortOrder=DESC&sortBy=CREATED_AT"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    # Initialize lists to store specific order attributes
    tokens = []
    names = []
    types = []
    states = []
    start_sending_at = []
    recipient_count = []
    delivered_count = []
    view_count = []
    click_count = []
    open_based_orders_count = []
    open_based_total_order_value = []
    click_based_orders_count = []
    click_based_total_order_value = []

    page_count = 1

    retry_count = 0

    while retry_count < 3:
        try:
            # Make the GET request to the API
            response = requests.get(endpoint, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                page_count = data["pagination_data"]["page_count"]

                # Loop through the order tiles
                for campaign in data["campaigns"]:
                    tokens.append(campaign["token"])
                    names.append(campaign["name"])
                    types.append(campaign["type"])
                    states.append(campaign["state"])
                    # if state is DRAFT, campaign doesn't have a start_sending_at and also doesn't have stats_v3
                    if campaign["state"] == "DRAFT" or campaign["state"] == "RUNNING":
                        start_sending_at.append(None)
                        recipient_count.append(None)
                        delivered_count.append(None)
                        view_count.append(None)
                        click_count.append(None)
                        open_based_orders_count.append(None)
                        open_based_total_order_value.append(None)
                        click_based_orders_count.append(None)
                        click_based_total_order_value.append(None)    
                    else:
                        start_sending_at.append(campaign["start_sending_at"])
                        campaign_statistics = {}
                        # some campaigns don't have stats_v3. They have stats_v2
                        if "stats_v3" in campaign:
                            campaign_statistics = campaign["stats_v3"]
                            delivered_count.append(campaign_statistics["delivered_count"])
                        elif "stats_v2" in campaign:
                            campaign_statistics = campaign["stats_v2"]
                            delivered_count.append(campaign_statistics["sent_count"])
                        
                        recipient_count.append(campaign_statistics["recipient_count"])
                        view_count.append(campaign_statistics["view_count"])
                        click_count.append(campaign_statistics["click_count"])
                        open_based_orders_count.append(campaign_statistics["open_based_orders_count"])
                        open_based_total_order_value.append(campaign_statistics["open_based_total_order_value"]["amount_cents"]/100)
                        click_based_orders_count.append(campaign_statistics["click_based_orders_count"])
                        click_based_total_order_value.append(campaign_statistics["click_based_total_order_value"]["amount_cents"]/100)
                break  # Successful request, exit the loop

            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/3)")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                print(f"Request failed with status code {response.status_code}")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
        except Exception as e:
            print(f"An error occurred: {e}")
            break
    return tokens, names, types, states, start_sending_at, recipient_count, delivered_count, view_count, click_count, open_based_orders_count, open_based_total_order_value, click_based_orders_count, click_based_total_order_value, page_count


def get_marketing_campaigns_info(brand_token, cookie):

    # Initialize lists to store specific order attributes
    tokens = []
    names = []
    types = []
    states = []
    start_sending_at = []
    recipient_count = []
    delivered_count = []
    view_count = []
    click_count = []
    open_based_orders_count = []
    open_based_total_order_value = []
    click_based_orders_count = []
    click_based_total_order_value = []

    page_number = 1
    tokens_page, names_page, types_page, states_page, start_sending_at_page, recipient_count_page, delivered_count_page, view_count_page, click_count_page, open_based_orders_count_page, open_based_total_order_value_page, click_based_orders_count_page, click_based_total_order_value_page, page_count = get_marketing_campaigns_info_page(page_number, brand_token, cookie)
    tokens.extend(tokens_page)
    names.extend(names_page)
    types.extend(types_page)
    states.extend(states_page)
    start_sending_at.extend(start_sending_at_page)
    recipient_count.extend(recipient_count_page)
    delivered_count.extend(delivered_count_page)
    view_count.extend(view_count_page)
    click_count.extend(click_count_page)
    open_based_orders_count.extend(open_based_orders_count_page)
    open_based_total_order_value.extend(open_based_total_order_value_page)
    click_based_orders_count.extend(click_based_orders_count_page)
    click_based_total_order_value.extend(click_based_total_order_value_page)

    if page_count > 1:
        for page_number in range(2, page_count + 1):
            tokens_page, names_page, types_page, states_page, start_sending_at_page, recipient_count_page, delivered_count_page, view_count_page, click_count_page, open_based_orders_count_page, open_based_total_order_value_page, click_based_orders_count_page, click_based_total_order_value_page, _ = get_marketing_campaigns_info_page(page_number, brand_token, cookie)

            tokens.extend(tokens_page)
            names.extend(names_page)
            types.extend(types_page)
            states.extend(states_page)
            start_sending_at.extend(start_sending_at_page)
            recipient_count.extend(recipient_count_page)
            delivered_count.extend(delivered_count_page)
            view_count.extend(view_count_page)
            click_count.extend(click_count_page)
            open_based_orders_count.extend(open_based_orders_count_page)
            open_based_total_order_value.extend(open_based_total_order_value_page)
            click_based_orders_count.extend(click_based_orders_count_page)
            click_based_total_order_value.extend(click_based_total_order_value_page)

    data = {
        "tokens": tokens,
        "names": names,
        "types": types,
        "states": states,
        "start_sending_at": start_sending_at,
        "recipient_count": recipient_count,
        "delivered_count": delivered_count,
        "view_count": view_count,
        "click_count": click_count,
        "open_based_orders_count": open_based_orders_count,
        "open_based_total_order_value": open_based_total_order_value,
        "click_based_orders_count": click_based_orders_count,
        "click_based_total_order_value": click_based_total_order_value
    }
    return data