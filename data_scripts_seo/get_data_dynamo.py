import requests
import pandas as pd
import time

from utils import (filter_unique_objects)

def get_rankings_query_for_day(query, day):

    endpoint_url = f"https://a0f2079rh1.execute-api.us-east-1.amazonaws.com/prod/search?executionDate={day}&searchQuery={query}"

    headers = {
        "x-api-key": "AAjmOO1_Kdl!!!Ssa1123a"
    }

    data = []

    retry_count = 0

    while retry_count < 3:

    # Make the GET request to the API
        try:
            response = requests.get(endpoint_url, headers=headers)

            data = response.json()

            if response.status_code == 200:
                if len(data) > 0:
                    data = filter_unique_objects(data)
                break    

            # we check the status of the response
            if response.status_code != 200:
                print("endpoint", endpoint_url)
                print(f"Error: {response.status_code} {response.text}")
                time.sleep(60)
                retry_count += 1
        except Exception as e:
            print(e)
            time.sleep(60)
            retry_count += 1

    return data

def get_rankings_query_for_period(query, dates):

    # dates is an array of dates in the format 'YYYY-MM-DD'

    # Initialize an empty list to store the DataFrames
    list_rankings = []

    for date in dates:
        # Get the rankings for each day
        print("date", date)
        rankings = get_rankings_query_for_day(query, date)

        for item in rankings:
            if 'min_option_retail_price' in item:
                del item['min_option_retail_price']
        
        # wait 3 seconds
        time.sleep(20)

        # Append the rankings DataFrame to the list
        list_rankings.append(rankings)

    flattened_list_rankings = [item for sublist in list_rankings for item in sublist]
    # Concatenate all DataFrames in the list into a single DataFrame
    df = pd.DataFrame(flattened_list_rankings)
    
    return df