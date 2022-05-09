import sys

sys.path.append("..")
import databaseEksamen.hbase.utility.data_for_generating as d
from databaseEksamen.hbase.entities.Product import Product

# Ja, det her import er scuffed, men du ved hvordan python er med imports :)(


def return_big_data_products():
    list_of_products = []
    for i in range(10000):
        p = Product(
            d.return_product_id(),
            d.return_grill_name(),
            d.return_brand_name(),
            d.return_item_number(),
            d.return_color(),
            d.return_grill_type(),
            d.return_amount_of_burners(),
            d.return_bread_basket(),
            d.return_amount_of_wheels(),
            d.return_length_in_cm(),
            d.return_width_in_cm(),
            d.return_price(),
        )
        list_of_products.append(p)
    return list_of_products
