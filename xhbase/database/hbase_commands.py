import happybase
import os


def connect():
        '''This returns our hbase connection'''
        connection = happybase.Connection(host = os.environ.get('HBASE_HOST'))
        return connection