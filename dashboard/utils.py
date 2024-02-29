import re
from datetime import datetime

def extract_date_from_filename(file_name):
    """
    Extracts the date from a file name in the format 'orders_from_api_YYYY-MM-DD'.
    
    Args:
    file_name (str): The name of the file.
    
    Returns:
    datetime object: The extracted date.
    None: If date is not found in the file name.
    """
    # Define a regular expression pattern to match the date
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    
    # Use regex to find the date pattern in the file name
    match = re.search(date_pattern, file_name)

    if match:
        # Extract the matched date string
        date_str = match.group(0)
        
        return date_str
    else:
        return None