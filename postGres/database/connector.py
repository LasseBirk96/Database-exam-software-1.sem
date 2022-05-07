from psycopg2 import connect

#establishing the connection

def establish_connection():
    conn = connect(
        host = "127.0.0.1",
        user = "dev",
        password = "dev123",
        dbname = "eksamen"
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
