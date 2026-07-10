import pandas as pd
from datetime import datetime

def transform_data(coins_df):

    coins_df = coins_df[
        [
            "name",
            "symbol",
            "rank",
            "last_update",
            "price_usd",
            "market_cap"
        ]
    ].copy()

    coins_df["last_update"] = pd.to_datetime(
        coins_df["last_update"],
        errors="coerce",
        utc=True
        )

    coins_df.rename(
        columns = {
            "id":"coin_id",
            "name":"coin_name"
        },
        inplace=True
    )

    coins_df.reset_index(drop=True, inplace=True)
    coins_df.sort_values("rank", inplace=True)

    return coins_df
