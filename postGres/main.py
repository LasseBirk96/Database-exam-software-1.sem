from webbrowser import get
import happybase
from connectorFiles.connector import establish_connection, get_version




def connect():
    connection = happybase.Connection(host='127.0.0.1')
    #ONLY RUN THIS ONCE, IF YOU HAVEN'T SET UP THE DATABÆSE
    connection.create_table('foods', {"cf1": dict()}) 
    table = connection.table('foods')
    return table



get_version(establish_connection())


connect()