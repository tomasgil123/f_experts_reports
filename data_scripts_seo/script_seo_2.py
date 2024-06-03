
import pandas as pd
import glob
from utils import (get_data_from_google_spreadsheet, generate_date_array)
from get_data_dynamo import (get_rankings_query_for_period)

from metrics import (get_brand_product_counts_top_100_per_date, get_brand_median_position_per_date)

from read_json import (load_seo_json, get_items_by_query_and_period)

brands = [
#   "Bon Artis",
#    "Caravan",
#    "Couleur Nature",
#    "Glimmer Wish",
   "Latico Leathers",
#   "Little Hometown",
#    "Lothantique",
#    "Shinesty",
#    "Trek Light",
#    "True Classic"
]

# - Evolution cantidad de productos en las primeras 100 lugares del ranking (done)
# - Por marca cuantos productos tiene entre los primeros 100 del ranking (done)
# - Evolution Ranking promedio
# - Evolution del ranking promedio por marca

# Todos
# - Hacer graficos
# - Dejar establecido proceso para actulizar datos (done)

# que graficos mostramos?

# - Evolucion Cantidad de productos en las primeras 100 posiciones del ranking para el cliente
# - Cantidad de productos en las primeras 100 posiciones del ranking para la competencia al dia de hoy
# - Evolucion del ranking promedio para el cliente
# - Ranking promedio para la competencia al dia de hoy

# yo quiero terminar con una sola dataframe que tenga 3 columnas:
# - execution_date, producto y posicion

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

    df_seo_total = pd.DataFrame()

    # we check if there is data already downloaded
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

        # Filter by selected brand_name and search_query
        filtered_df = df_rankings[(df_rankings['brand_name'] == brand) & (df_rankings['search_query'] == query)]

        # Filter for top 100 results
        top_100_df = filtered_df[filtered_df['order'] <= 100]

        # Select required columns
        result_df = top_100_df[['execution_date', 'title', 'order', 'search_query']]

        # we add the results to df_seo dataframe
        df_seo_total = pd.concat([df_seo_total, result_df])
    
    if len(seo_rankings_file) > 0:
        df_seo_prev = pd.read_csv(seo_rankings_file[0])

        # we concatenate the new df_count with the old one
        df_seo_total = pd.concat([df_seo_prev, df_seo_total])
        # we download the dataframe as csv
        df_seo_total.to_csv(name_seo_rankings_file, index=False)
    else:
        df_seo_total.to_csv(name_seo_rankings_file, index=False)

        


