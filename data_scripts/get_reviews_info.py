import requests
import time

def get_reviews_data_for_page(brand_token, page_number):
    # Define the API endpoint URL
    endpoint_url = f"https://www.faire.com/api/brand/reviews/{brand_token}?page={page_number}&pageSize=50&viewAsRetailer=true"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    }

    # Initialize lists to store the specific product attributes
    tokens = []
    publish_at_values = []
    created_at_values = []
    #metrics_data = {}
    ratings = []
    titles = []

    retry_count = 0
    max_retries = 3

    while retry_count < max_retries:
        try:
            # Make the POST request to the API
            response = requests.get(endpoint_url, headers=headers)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the JSON response
                data = response.json()

                page_count = data["pagination_data"]["page_count"]

                # Loop through the product tiles
                for review in data["brand_reviews"]:
                     tokens.append(review["token"])
                     publish_at_values.append(review["publish_at"])
                     created_at_values.append(review["created_at"])
                    
                    #  for metric in review["metrics"]:
                    #     metrics_data[metric["label"]].append(metric["selected"])
                    
                     ratings.append(review["rating"])
                     # if title exists
                     if "title" in review:
                        titles.append(review["title"])
                     else:
                        titles.append("")
                break  # Successful request, exit the loop
            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/{max_retries})")
                time.sleep(30)  # Wait for 30 seconds before retrying
                retry_count += 1
            else:
                print(f"Request failed with status code {response.status_code}")
                break  # Exit the loop on other errors
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit the loop on other exceptions
    print("titles", titles)
    return tokens, publish_at_values, created_at_values, titles, ratings, page_count


def get_reviews_info(brand_token):
    # Initialize lists to store reviews data
    tokens = []
    publish_at_values = []
    created_at_values = []
    #metrics_data = []
    titles = []
    ratings = []
    page_count = 1

    # we loop over the different pages and get the reviews info
    page_number = 1
    tokens_page, publish_at_values_page, created_at_values_page, titles_page, ratings_page, page_count = get_reviews_data_for_page(brand_token, page_number)
    tokens.extend(tokens_page)
    publish_at_values.extend(publish_at_values_page)
    created_at_values.extend(created_at_values_page)
    #metrics_data.extend(metrics_data_page)
    titles.extend(titles_page)
    ratings.extend(ratings_page)

    if page_count > 1:
            for page in range(2, page_count + 1):
                print(f"Fetching page {page}/{page_count}")
                print("----------------")
                tokens_page, publish_at_values_page, created_at_values_page, titles_page, ratings_page, page_count = get_reviews_data_for_page(brand_token, page)
                tokens.extend(tokens_page)
                publish_at_values.extend(publish_at_values_page)
                created_at_values.extend(created_at_values_page)
                #metrics_data.extend(metrics_data_page)
                titles.extend(titles_page)
                ratings.extend(ratings_page)
                time.sleep(10)  # Sleep for 30 second between requests

    data = {
        "tokens": tokens,
        "publish_at_values": publish_at_values,
        "created_at_values": created_at_values,
       #"metrics_data": metrics_data,
        "titles": titles,
        "ratings": ratings
    }
    return data