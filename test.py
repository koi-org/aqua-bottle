import os
from dotenv import load_dotenv, find_dotenv
from psycopg_pool import ConnectionPool
from psycopg import errors

# Load environment variables
env_path = find_dotenv(usecwd=True)
if env_path:
    print(f"Loading .env file from: {env_path}")
    load_dotenv(dotenv_path=env_path, verbose=True, override=True)
else:
    print("No .env file found in current working directory or parent directories.")

DATABASE_URI = os.getenv("DATABASE_URI")

if not DATABASE_URI:
    print("Critical: DATABASE_URI not set in environment or .env file. Exiting.")
    exit(1)

pool = None
try:
    pool = ConnectionPool(DATABASE_URI, min_size=1, max_size=5)

    # Test connection
    with pool.connection() as conn:
        print("Successfully connected to the database!")
        with conn.cursor() as cur:
            cur.execute("SELECT version();")
            db_version = cur.fetchone()
            print(f"Database version: {db_version[0] if db_version else 'N/A'}")
            print("Successfully created a cursor and executed a test query!")

except Exception as e:
    print(f"Failed to initialize connection pool or connect: {e}")
    # If pool initialization fails, we shouldn't proceed.
    exit(1)


def clear_databases():
    if not pool:
        print("Pool not initialized. Cannot clear databases.")
        return
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                print("Attempting to clear tables...")
                cur.execute('DELETE FROM "Aquariums"')
                cur.execute('DELETE FROM "Fishes"')
                cur.execute('DELETE FROM "Plants"')
                cur.execute('DELETE FROM "Users"')  #
                print("Successfully cleared tables!")
            except Exception as e:
                print(f"An unexpected error occurred during table clearing: {e}")


def add_user(userid: str, username: str):
    if not pool:
        print("Pool not initialized. Cannot add user.")
        return
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                # Use parameter substitution to prevent SQL injection
                query = 'INSERT INTO "Users" (id, username) VALUES (%s, %s)'
                cur.execute(query, (userid, username))
                print(f"Successfully added user: ID={userid}, Username={username}")
            except Exception as e:
                print(f"An unexpected error occurred while adding user: {e}")


def add_aquarium(aquariumid: int, user_id: str):
    assert pool is not None
    with pool.connection() as conn:
        with conn.cursor() as cur:
            try:
                print("attempting to insert aquarium")
                query = 'insert into "Aquariums" (id, "user") values (%s, %s)'
                cur.execute(query, (aquariumid, user_id))
                print("inserted aquarium!")
            except Exception as e:
                print(e)


# --- Main script execution ---
if __name__ == "__main__":
    print("\n--- Running database operations ---")

    print("\nClearing databases...")
    clear_databases()

    print("\nAdding users...")
    add_user("1233432", "Bob")
    add_user("9876543", "Alice")
    # add_user("1233432", "Charlie")

    add_aquarium(1, "9876543")

    print("\n--- Script finished ---")

    if pool:
        print("Closing connection pool...")
        pool.close()
        print("Connection pool closed.")
