import pandas as pd
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import glob
from get_product_views_info import (get_page_views_for_all_months_since_date)
from cookie import (cookie_token)


brand_name = "true_classic"
# brand_name = "couleur_nature"
# brand_name = "caravan"
# brand_name = "bon_artis"
# brand_name = "lothantique"
# brand_name = "shinesty"
# brand_name = "glimmer_wish"
# brand_name = "trek_light"
# brand_name = "latico_leathers"
# brand_name = "little_hometown"
# brand_name = "be_huppy"

#product_views_file = glob.glob(f"../dashboard/dashboard_data/{brand_name}/page_views_info_*.csv")
product_views_file= []

if len(product_views_file) > 0:
    df_current_product_views = pd.read_csv(product_views_file[0])

    # Parse the date column
    df_current_product_views['date'] = pd.to_datetime(df_current_product_views['date'])

    # Get the current date
    current_date = datetime.now()

    current_formatted_date = current_date.strftime("%Y-%m-01")

    # Get the first day of the current month
    first_day_current_month = current_date.replace(day=1)

    # Get the first day of the previous month
    first_day_previous_month = (first_day_current_month - timedelta(days=1)).replace(day=1)

    # Get the first day of the month before the previous month
    first_day_previous_previous_month = first_day_previous_month - relativedelta(months=1)

    formatted_first_day_previous_month = first_day_previous_month.strftime("%Y-%m-%d")

    # Filter out rows from the current and previous months
    filtered_df = df_current_product_views[(df_current_product_views['date'] < first_day_previous_previous_month)]

    data = get_page_views_for_all_months_since_date(cookie=cookie_token, starting_date=formatted_first_day_previous_month)

    data_df = pd.DataFrame(data)
    # we add data rows to filtered_df dataframe
    combined_df = pd.concat([filtered_df, data_df])

    # Reset the index if necessary
    combined_df.reset_index(drop=True, inplace=True)

    # get today date
    today = pd.to_datetime('today').date()
    # convert it to a string with format yyyy/mm/dd
    today = today.strftime('%Y-%m-%d')

    name_csv = f'../dashboard/dashboard_data/{brand_name}/page_views_info_{today}.csv'

    # we doenload it to a  csv
    combined_df.to_csv(name_csv, index=False)
else:
    data = get_page_views_for_all_months_since_date(cookie=cookie_token, starting_date="2023-01-01")

    # we create a new dataframe
    df = pd.DataFrame(data)
    # we download it as a csv

    # get today date
    today = pd.to_datetime('today').date()
    # convert it to a string with format yyyy/mm/dd
    today = today.strftime('%Y-%m-%d')

    name_csv = f'../dashboard/dashboard_data/{brand_name}/page_views_info_{today}.csv'

    df.to_csv(name_csv, index=False)

