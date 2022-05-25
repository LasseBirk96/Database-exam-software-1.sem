from psycopg2 import connect
import os

#establishing the connection

def establish_connection():
    conn = connect(
        dbname = os.environ.get('POSTGRES_DB'),
        user = os.environ.get('POSTGRES_USER'),
        password = os.environ.get('POSTGRES_PASSWORD'),
        host = os.environ.get('POSTGRES_HOST'),
        port = os.environ.get('POSTGRES_PORT')
    )
    return conn

def get_version(conn):
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Executing an MYSQL function using the execute() method
    cursor.execute("select version()")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    print("Connection established to: ", data)

    #Closing the connection
    conn.close()
