import happybase
from utility import product_generator


def connect():
    try:
        connection = happybase.Connection(host="127.0.0.1")
        return connection
    except:
        print(
            "This is a horrible error message that is only temporary, but if you see it, you are most likely connected to hbase"
        )


def create_table():
    connection = connect()
    connection.create_table("products", {"product_id": dict()})
    table = connection.table("products")
    return table


def populate_table(table):
    table = create_table()
    batcher = table.batch()
    products = product_generator.return_big_data_products()

    for element in products:
        id = element.return_product()["product_id"]
        column_string = str(f"product_id:{id}")
        batcher.put(b"product", {column_string: str(element.return_product())})
    batcher.send()

    table = create_table()
    populate_table(table)


connection = connect()
table = connection.table("products")

rows = table.rows([b"product"])
for key, data in rows:
    print(data)  # This one prints all that data
    print(
        data[b"product_id:ffd635b7-828f-467b-abea-e719c4347eb4"]
    )  # This prints the dictionary with this specific id
