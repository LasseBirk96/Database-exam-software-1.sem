'''THIS CLASS ENABLES US TO CONNECT TO OUR POSTGRES'''
import os
from psycopg2 import connect


def establish_connection():
    '''This method allows us to connect to our docker-postgres service'''
    conn = connect(
        dbname = os.environ.get('POSTGRES_DB'),
        user = os.environ.get('POSTGRES_USER'),
        password = os.environ.get('POSTGRES_PASSWORD'),
        host = os.environ.get('POSTGRES_HOST'),
        port = os.environ.get('POSTGRES_PORT')
    )
    return conn
