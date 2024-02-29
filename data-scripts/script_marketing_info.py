import pandas as pd
from get_marketing_campaigns_info import (get_marketing_campaigns_info)
from cookie import (cookie_token)

brand_token = "b_cad0ccd3"

marketing_campaign_info = get_marketing_campaigns_info(brand_token, cookie=cookie_token)

# we convert orders_info to a dataframe and then we download it as csv
df = pd.DataFrame(marketing_campaign_info)
df.to_csv('marketing_campaign_info.csv', index=False)