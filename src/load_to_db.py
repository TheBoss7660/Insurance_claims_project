import pandas as pd
from database import create_db_engine

df= pd.read_csv('..data/processed/..')

df.to_sql(
    name='table_name',
    con=engine,
    if_exists='append',
    index=False
)

print('Data loaded successfully to the database.')