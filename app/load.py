from database import engine

def load_data(coins_df):

    coins_df.to_sql(
        "paprika_coins",
        con=engine,
        if_exists="replace",
        index=False
    )

    print("Data loaded successfully.")