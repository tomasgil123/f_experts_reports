import os
import pandas as pd

# Define a function to extract the brand name from the file name
def extract_brand_name(filename):
    brand_name = filename.split('_')[0]
    return brand_name

# Directory where your CSV files are located
csv_directory = './'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Create an empty DataFrame to store the merged data
merged_data = pd.DataFrame()

# Iterate through each CSV file, extract the brand name, and add it as a new column
for csv_file in csv_files:
    brand_name = extract_brand_name(csv_file)
    file_path = os.path.join(csv_directory, csv_file)
    
    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Add a new column 'brand' with the brand name
    df['brand'] = brand_name
    
    # Append the data to the merged_data DataFrame
    merged_data = pd.concat([merged_data, df], ignore_index=True)

# Save the merged data to a new CSV file
merged_data.to_csv('products.csv', index=False)

print("Merged CSV file saved as 'merged_products.csv'")
