import requests
import time

def get_reviews_page(brand_token, cookie, page_number):
    url_endpoint = f"https://www.faire.com/api/brand/reviews/{brand_token}?page={page_number}&pageSize=10&sortBy=CREATED_AT&requestedSortOrder=DESC"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': cookie
    }

    token = []
    brand_order_token = []
    rating = []
    comment = []
    replies = []
    retailer_name = []
    created_at = []
    publish_at = []

    page_count = 1
    retry_count = 0
    rate_limit_hits = 0

    while retry_count < 3:
        try:
            response = requests.get(url_endpoint, headers=headers)
            if response.status_code == 200:
                data = response.json()
                page_count = data["pagination_data"]["page_count"]

                for review in data["brand_reviews"]:
                    token.append(review.get("token", None))
                    brand_order_token.append(review.get("brand_order_token", None))
                    rating.append(review.get("rating", None))
                    
                    title = review.get("title", "")
                    comments = review.get("comment", "")
                    title_comment = title + " " + comments

                    comment.append(title_comment)
                    replies.append(len(review.get("replies", [])))
                    retailer_name.append(review.get("retailer_name", None))
                    created_at.append(review.get("created_at", None))
                    publish_at.append(review.get("publish_at", None))
                
                break

            elif response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in 30 seconds (Retry {retry_count + 1}/3)")
                time.sleep(30)
                retry_count += 1
                rate_limit_hits += 1
                
                ip_suffix = rate_limit_hits + 1
                headers.update({
                    'X-Originating-IP': f'127.0.0.{ip_suffix}',
                    'X-Forwarded-For': f'127.0.0.{ip_suffix}',
                    'X-Remote-IP': f'127.0.0.{ip_suffix}',
                    'X-Remote-Addr': f'127.0.0.{ip_suffix}',
                    'X-Client-IP': f'127.0.0.{ip_suffix}',
                    'X-Host': f'127.0.0.{ip_suffix}',
                    'X-Forwarded-Host': f'127.0.0.{ip_suffix}'
                })
            else:
                print(f"Request failed with status code {response.status_code}")
                return None, 0  # Return None and 0 to indicate failure
        except Exception as e:
            print(f"An error occurred: {e}")
            return None, 0  # Return None and 0 to indicate failure

    data = {
        "token": token,
        "brand_order_token": brand_order_token,
        "rating": rating,
        "comment": comment,
        "replies": replies,
        "retailer_name": retailer_name,
        "created_at": created_at,
        "publish_at": publish_at
    }
    return data, page_count

def find_first_older_date_index(created_at, time_most_recent_review):
    for index, date in enumerate(created_at):
        if date is not None and date < time_most_recent_review * 1000:  # Convert to milliseconds
            return index
    return -1

def get_reviews(brand_token, cookie, time_most_recent_review):
    all_data = {
        "token": [],
        "brand_order_token": [],
        "rating": [],
        "comment": [],
        "replies": [],
        "retailer_name": [],
        "created_at": [],
        "publish_at": []
    }

    page_number = 1

    while True:
        data, page_count = get_reviews_page(brand_token, cookie, page_number)
        
        if data is None:
            print("Failed to fetch data. Stopping.")
            break

        created_at_page = data["created_at"]

        first_older_date_index = find_first_older_date_index(created_at_page, time_most_recent_review)

        if first_older_date_index == -1:
            for key in all_data.keys():
                all_data[key].extend(data[key])
        else:
            for key in all_data.keys():
                all_data[key].extend(data[key][:first_older_date_index])
            break

        if page_number >= page_count:
            break
        
        time.sleep(20)
        page_number += 1
        print(f"Pages left: {page_count - page_number}")

    return all_data