import sys
sys.path.append("..")
from .connector import establish_connection


# Allows us to set up any table in postgres that we might want. However in this case, we will never need more than just the user_table
def set_up_table(command):
    conn = establish_connection()
    cur = conn.cursor()
    try:
        cur.execute(command)
        cur.close()
        conn.commit()
        print("Successfully created table")
    except (Exception) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

# Returns the sql query that creates a user_table
def return_user_table():
    user_table = """
    CREATE TABLE IF NOT EXISTS users (
	user_id VARCHAR(255) primary KEY,
        first_name VARCHAR(255) not NULL,
        last_name VARCHAR(255) not NULL,
        password VARCHAR(255) not NULL,
        age SMALLINT not NULL,
        email VARCHAR(255) unique not NULL,
        phonenumber VARCHAR(255) unique not NULL
    );
    """
    return user_table


def set_up_user_table():
    user_table = return_user_table()
    set_up_table(user_table)
