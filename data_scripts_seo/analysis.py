import pandas as pd
import glob

df_base = pd.read_csv('./ebase_execution_records_2024-06-24.csv')

# Adjust the path to where your files are located
path = './'  # use your path
all_files = glob.glob(path + "execution_records_2024-*.csv")

# List to hold the dataframes
queries_data = []
number_products_remain_ranking = []
number_products_better_ranking = []
number_products_worse_ranking = []
number_products_same_ranking = []
number_products_better_median = []
number_products_worse_median = []

print("all_files", all_files)

# Loop through the file list and read each file into a dataframe, then append it to the list
for index, file in enumerate(all_files):
    df = pd.read_csv(file)

    # we have to loop over the search queries
    queries = ["Crossbody Bags", "Tote Bag", "Wallets", "Shoulder Bags", "Backpack"]

    for query in queries:

        df_query_base = df_base[df_base['search_query']== query]
        df_query = df[df['search_query']== query]

        df_merge = pd.merge(df_query_base, df_query[['title', 'order']], on='title', how='left')

        # we remove products without order_y value
        df_merge = df_merge.dropna(subset=['order_y'])

        df_merge['better'] = df_merge['order_x'] > df_merge['order_y']
        df_merge['worse'] = df_merge['order_x'] < df_merge['order_y']
        df_merge['difference'] = df_merge['order_y'] - df_merge['order_x']

        # download dataframe as a csv
        if query == 'Crossbody Bags':
            df_merge.to_csv(f"ranking_comparison_{query}_{index}.csv", index=False)

        remain = df_merge.shape[0]
        better = (df_merge['order_x'] > df_merge['order_y']).sum()
        better_median = df_merge[df_merge['better'] == True]['difference'].median()
        worse = (df_merge['order_x'] < df_merge['order_y']).sum()
        worse_median = df_merge[df_merge['worse'] == True]['difference'].median()
        same = (df_merge['order_x'] == df_merge['order_y']).sum()

        queries_data.append(query)
        number_products_remain_ranking.append(remain)
        number_products_better_ranking.append(better)
        number_products_worse_ranking.append(worse)
        number_products_same_ranking.append(same)
        number_products_better_median.append(better_median)
        number_products_worse_median.append(worse_median)
    
    # df_base is the last dataframe read
    df_base = df

results = {
    'search_query': queries_data,
    'number_products_remain_ranking': number_products_remain_ranking,
    'number_products_better_ranking': number_products_better_ranking,
    'number_products_worse_ranking': number_products_worse_ranking,
    'number_products_same_ranking': number_products_same_ranking,
    'number_products_better_median': number_products_better_median,
    'number_products_worse_median': number_products_worse_median
}

df_results = pd.DataFrame(results)

# download dataframe
df_results.to_csv("ranking_comparison_results.csv", index=False)