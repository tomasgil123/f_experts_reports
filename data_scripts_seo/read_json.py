import json
import pandas as pd

def load_seo_json():

    # Specify the path to your JSON file
    file_path = './data/seo.json'
    # Initialize a list to store the parsed JSON objects
    data = []

    # Open and read the JSON file line by line
    with open(file_path, 'r') as file:
        for line in file:
            item = json.loads(line.strip())
            reformatted_item = {
                "search_query": item["Item"]["search_query"]["S"],
                "brand_token": item["Item"]["brand_token"]["S"],
                "sort_key": item["Item"]["sort_key"]["S"],
                "execution_date": item["Item"]["execution_date"]["S"],
                "brand_name": item["Item"]["brand_name"]["S"],
                "execution_timestamp": item["Item"]["execution_timestamp"]["S"],
                "order": int(item["Item"]["order"]["N"]),
                "title": item["Item"]["title"]["S"]
            }
            data.append(reformatted_item)

    return data

# data = load_seo_json()

# # print first 5 items
# print(data[:5])


def get_items_by_query_and_period(data, search_query, dates):
    """
    Get items that match the given search query and dates.

    Args:
        data (list): A list of JSON objects.
        search_query (str): The search query to match.
        dates (list): A list of execution dates to match.

    Returns:
        list: A list of matching JSON objects.
    """
    matching_items = [item for item in data if item["search_query"] == search_query and item["execution_date"] in dates]

    df = pd.DataFrame(matching_items)
    
    return df