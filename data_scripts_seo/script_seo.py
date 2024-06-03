
import pandas as pd
import glob
from utils import (get_data_from_google_spreadsheet, generate_date_array)
from get_data_dynamo import (get_rankings_query_for_period)

from metrics import (get_brand_product_counts_top_100_per_date, get_brand_median_position_per_date)

from read_json import (load_seo_json, get_items_by_query_and_period)

brands = [
#  "Bon Artis",
#   "Caravan",
#   "Couleur Nature",
   "Glimmer Wish",
#   "Latico",
#   "Little Hometown",
#   "Lothantique",
#   "Shinesty",
#   "Trek Light",
#   "True Classic"
]

does_api_work = False

seo_data = []

if does_api_work is False:
    seo_data = load_seo_json()

spreadsheet_id = '1yN0KXGaGTBIjx9VwRAc-ce9WS6dBgwSel1Jf7qWiInA'  # Please set the Spreadsheet ID.
range_name = 'Main'  # Example sheet name
df_queries = get_data_from_google_spreadsheet(spreadsheet_id, range_name)

for brand in brands:

    df_queries_brand = df_queries[df_queries['Brand'] == brand]

    queries = df_queries_brand['Query'].tolist()
    brand = df_queries_brand['Brand'].tolist()[0]

    df_counts_total = pd.DataFrame()
    df_median_position_total = pd.DataFrame()
    df_rankings_last_day_total = pd.DataFrame()

    # # we check if there is data already downloaded
    name_seo_rankings_file = f"../dashboard/dashboard_data/{brand.lower().replace(' ', '_')}/seo_rankings.csv"
    seo_rankings_file = glob.glob(name_seo_rankings_file)

    start_date = "2024-05-22"
    
    # we want to start getting new data since the last date we have data
    if len(seo_rankings_file) > 0:

        df_rankings_prev = pd.read_csv(seo_rankings_file[0])
        # we identify the last execution date
        last_execution_date = df_rankings_prev['execution_date'].max()

        start_date = last_execution_date
    
    dates = generate_date_array(start_date)

    # for query in queries we get rankings
    for query in queries:

        # we print combination of query and date
        print(f"Getting rankings for {query} on {dates}")

        if does_api_work is True:
            df_rankings = get_rankings_query_for_period(query, dates)
        else:
            df_rankings = get_items_by_query_and_period(seo_data, query, dates)
            #print(df_rankings)

        # we select the last day of the rankings
        df_rankings_last_day = df_rankings.copy()
        df_rankings_last_day = df_rankings[df_rankings['execution_date'] == dates[-1]]
        df_rankings_last_day['query'] = query

        print("length df_rankings_last_day", len(df_rankings_last_day))

        # we concat this dataframe to df_rankings_last_day_total
        df_rankings_last_day_total = pd.concat([df_rankings_last_day_total, df_rankings_last_day])

        for date in dates:

            df_rankings_date = df_rankings[df_rankings['execution_date'] == date]

            print(df_rankings_date.head())
            print("length df_rankings_date", len(df_rankings_date))

            if len(df_rankings_date) == 0:
                continue
            
            df_counts = get_brand_product_counts_top_100_per_date(df_rankings_date)
            df_counts['query'] = query

            df_median_position = get_brand_median_position_per_date(df_rankings_date)
            df_median_position['query'] = query

            df_counts_total = pd.concat([df_counts_total, df_counts])
            df_median_position_total = pd.concat([df_median_position_total, df_median_position])
    
    # we store all dataframes as csvs
    name_seo_count_file = f"../dashboard/dashboard_data/{brand.lower().replace(' ', '_')}/seo_count.csv"
    seo_count_file = glob.glob(name_seo_count_file)
    name_seo_position_file = f"../dashboard/dashboard_data/{brand.lower().replace(' ', '_')}/seo_positions.csv"
    seo_position_file = glob.glob(name_seo_position_file)

    if len(seo_count_file) > 0:
        df_count_prev = pd.read_csv(seo_count_file[0])

        # we concatenate the new df_count with the old one
        df_counts_total = pd.concat([df_count_prev, df_counts_total])
        # we download the dataframe as csv
        df_counts_total.to_csv(name_seo_count_file, index=False)
    else:
        df_counts_total.to_csv(name_seo_count_file, index=False)
    
    if len(seo_position_file) > 0:
        df_position_prev = pd.read_csv(seo_position_file[0])

        # we concatenate the new df_count with the old one
        df_median_position_total= pd.concat([df_position_prev, df_median_position_total])
        # we download the dataframe as csv
        df_median_position_total.to_csv(name_seo_position_file, index=False)
    else:
        df_median_position_total.to_csv(name_seo_position_file, index=False)

    df_rankings_last_day_total.to_csv(name_seo_rankings_file, index=False)