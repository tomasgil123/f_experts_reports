
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

    df_seo_top_10 = pd.DataFrame()

    # we check if there is data already downloaded
    name_seo_rankings_file = f"../dashboard/dashboard_data/{brand.lower().replace(' ', '_')}/seo_rankings_top_10.csv"
    seo_rankings_file = glob.glob(name_seo_rankings_file)

    start_date = "2024-05-22"

    dates = generate_date_array(start_date)

    # for query in queries we get rankings
    for query in queries:

        # we print combination of query and date
        print(f"Getting rankings for {query} on {dates}")

        if does_api_work is True:
            df_rankings = get_rankings_query_for_period(query, dates)
        else:
            df_rankings = get_items_by_query_and_period(seo_data, query, dates)

        df_top_10_products_start_date = df_rankings[df_rankings['execution_date'] == dates[0]].nsmallest(10, 'order')

        top_10_products_list = df_top_10_products_start_date['title'].tolist()

        # we filter df_rankings by top_10_products_list
        df_rankings = df_rankings[df_rankings['title'].isin(top_10_products_list)]

        # we keep only this columns 'execution_date', 'title', 'order', 'search_query'
        df_rankings = df_rankings[['execution_date', 'title', 'order', 'search_query']]

        df_seo_top_10 = pd.concat([df_seo_top_10, df_rankings])

# we download the dataframe to a csv
df_seo_top_10.to_csv(name_seo_rankings_file, index=False)

