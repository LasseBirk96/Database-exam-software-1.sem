'''THIS CLASS IS FOR GENERATING PRODUCTS'''
import sys

sys.path.append("xhbase")
from data_generator import data_for_generating as d
from xhbase.entities.Product import Product


def return_big_data_products(amount_data_products_to_be_generated):
    '''Returns a list of generated products'''
    list_of_products = []
    for i in range(amount_data_products_to_be_generated):
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
