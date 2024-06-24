import requests
from datetime import datetime
import os
import csv
from seo_cookie import cookie
import time

def map_api_response_to_execution_records(response, query, execution_date, execution_timestamp):
    product_tiles = response.json()['product_tiles']
    brands_by_token = response.json()['brands_by_token']

    execution_records = []
    for index, tile in enumerate(product_tiles):
        #print("tile", tile)
        execution_record = {
            'title': tile['product']['name'],
            'sort_key': f"{query}:{execution_timestamp}:{index + 1}",
            'brand_token': tile['product']['brand_token'],
            'brand_name': brands_by_token.get(tile['product']['brand_token'], {}).get('name'),
            'min_option_retail_price': tile['min_option_retail_price'],
            'order': index + 1,
            'execution_date': execution_date,
            'execution_timestamp': execution_timestamp,
            'search_query': query
        }
        execution_records.append(execution_record)
    return execution_records

def process_queries(queries):
    now = datetime.utcnow()
    execution_date = now.strftime("%Y-%m-%d")
    execution_timestamp = now.isoformat()

    all_execution_records = []

    for query in queries:
        print(f"Processing query: {query}")
        try:
            headers = {
                "Content-Type": "application/json",
                "Cache-Control": "no-cache",
                "User-Agent": "PostmanRuntime/7.36.3",
                "Accept": "*/*",
                "Accept-Encoding": "gzip, deflate, br",
                "Connection": "keep-alive",
                "Cookie": cookie,
            }

            payload = {
                "query": query,
                "page_number": 0,
                "page_size": 100
            }

            response = requests.post(
                os.getenv('SEARCH_ENDPOINT', 'https://www.faire.com/api/v3/search/products'),
                json=payload,
                headers=headers
            )
            print(f"Received response for query: {query}. Status: {response.status_code}")

            execution_records = map_api_response_to_execution_records(
                response, query, execution_date, execution_timestamp
            )

            print("executionRecords length: ", len(execution_records))
            all_execution_records.extend(execution_records)

        except requests.exceptions.RequestException as e:
            if e.response:
                print(f"Error processing query: {query}. Status code: {e.response.status_code}")
                print(f"Response body: {e.response.text}")
            else:
                print(f"An unexpected error occurred: {e}")
        time.sleep(15)

    save_execution_record(all_execution_records, execution_date)

def save_execution_record(records, execution_date):
    filename = f"execution_records_{execution_date}.csv"
    keys = records[0].keys() if records else []
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)
    
    print(f"Saved execution records to {filename}")

# Example usage
queries = ["Crossbody Bags", "Tote Bag", "Wallets", "Shoulder Bags", "Backpack"]



process_queries(queries)
