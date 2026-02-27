from sqlalchemy import create engine

def create_db_engine():
    username = 'postgres'
    password = 'bosire'
    host = 'localhost'
    port = '5432'
    database = 'insurance_db'

    engine= create_engine (
        f'postgresql://{username}:{password}@{host}:{port}/{database}'
    )

    return engine