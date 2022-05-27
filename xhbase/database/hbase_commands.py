import happybase
import os


def connect():
        connection = happybase.Connection(host = os.environ.get('HBASE_HOST'))
        return connection