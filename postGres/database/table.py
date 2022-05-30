"""THIS CLASS DOES THINGS WITH OUR POSTGRES"""
import sys

sys.path.append("..")
from .connector import establish_connection


def set_up_table(command):
    """This methods allows us to execute on or more quieres.
    However, in our case it is only used to set up one table"""
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


def return_user_table():
    """This method returns the SQL for creating a table called users"""
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
    """This method creates and sets up our table"""
    user_table = return_user_table()
    set_up_table(user_table)
