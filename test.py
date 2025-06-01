import os
from dotenv import load_dotenv, find_dotenv # Import find_dotenv
from psycopg_pool import ConnectionPool

env_path = find_dotenv(usecwd=True)
loaded_successfully = load_dotenv(dotenv_path=env_path, verbose=True, override=True)

DATABASE_URI_FROM_ENV = os.getenv('DATABASE_URI')

try:
    print(f"Attempting to connect with URI: '{DATABASE_URI_FROM_ENV}'")
    pool = ConnectionPool(DATABASE_URI_FROM_ENV)

    with pool.connection() as conn:
        print("Successfully connected to the database!")
        with conn.cursor() as cur:
            cur.execute("SELECT * from User;") 
            print(cur.fetchone())
except Exception as e:
    print(f"Failed to connect or execute query: {e}")