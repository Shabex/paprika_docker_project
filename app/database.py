from config import *
from sqlalchemy import create_engine

DATABASE_URL = (
    f"postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}"
    f"@{DATABASE_HOST}:{DATABSE_PORT}/{DATABASE_NAME}"
    )

engine = create_engine(DATABASE_URL)
