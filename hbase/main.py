import happybase

def connect():
    try:
        connection = happybase.Connection(host='127.0.0.1')
        #ONLY RUN THIS ONCE, IF YOU HAVEN'T SET UP THE DATABÆSE
        connection.create_table('foods', {"cf1": dict()}) 
        table = connection.table('foods')
        print("CONNECTION SUCCESSFUL")
        print(connection)
        return table
    except:
        print("This is a horrible error message that is only temporary, but if you see it, you are most likely connected to hbase")

connect()