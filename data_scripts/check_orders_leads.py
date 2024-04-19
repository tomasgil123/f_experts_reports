import pandas as pd

# we load coleaur nature leads csv
#df_leads = pd.read_csv('Caravan_leads.csv')
#df_leads = pd.read_csv('Coleur_nature_leads.csv')
#df_leads = pd.read_csv('true_classic_leads.csv')
#df_leads = pd.read_csv('bon_artis_leads.csv')
df_leads = pd.read_csv('lothantique_leads.csv')

# convert column "Name" to lower case
df_leads['Name'] = df_leads['Name'].str.lower()

#brand_name = "caravan"
#brand_name = "couleur_nature"
#brand_name = "true_classic"
#brand_name = "bon_artis"
brand_name = "lothantique"

# we load orders from coleur nature
df_orders = pd.read_csv(f'../dashboard/dashboard_data/{brand_name}/orders_from_api_2024-04-15.csv')

# convert column "retailer_names" to lower case
df_orders['retailer_names'] = df_orders['retailer_names'].str.lower()

# we do a left join of leads and orders using column "Name" and "retailer_names"
df_leads_orders = pd.merge(df_leads, df_orders, left_on='Name', right_on='retailer_names', how='left')

# filter rows where "retailer_names" is not null
df_leads_orders = df_leads_orders[df_leads_orders['retailer_names'].notnull()]

print(df_leads_orders)

