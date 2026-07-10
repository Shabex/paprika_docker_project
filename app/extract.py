import requests
import pandas as pd
from config import *

def extract_data():

    url = API_URL

    response = requests.get(url)


    data = response.json()

    # print(data[0])

    rows = []
    for coin in data:
        if coin["symbol"] in ["BTC","ETH","USDT","BNB","USDC","GAL","UTK","MAPO","BTX"]:
            rows.append({
                "id":coin["id"],
                "name":coin["name"],
                "symbol": coin["symbol"],
                "rank": coin["rank"],
                "last_update": coin.get("last_updated",{}),
                "price_usd" : coin.get("quotes", {}).get("USD", {}).get("price"),
                "market_cap" : coin.get("quotes",{}).get("USD",{}).get("market_cap")

            })

    coins_df = pd.DataFrame(rows)

    return coins_df
    # print(coins_df)