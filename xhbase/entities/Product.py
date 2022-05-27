class Product:
    def __init__(self, product_id, product_name, product_brand, item_number, color, grill_type, amount_of_burners, bread_basket, amount_of_wheels, length_in_cm, width_in_cm, product_price):
        self.product_id = product_id
        self.product_name = product_name
        self.product_brand = product_brand
        self.item_number = item_number
        self.color = color
        self.grill_type = grill_type
        self.amount_of_burners = amount_of_burners
        self.bread_basket =  bread_basket
        self.amount_of_wheels = amount_of_wheels
        self.length_in_cm = length_in_cm
        self.width_in_cm = width_in_cm
        self.product_price = product_price
        
        

    def return_product(self):
        return {"product_id": self.product_id, 
                "product_name": self.product_name,
                "product_brand": self.product_brand, 
                "item_number" : self.item_number,
                "color" : self.color,
                "grill_type" : self.grill_type,
                "amount_of_burners" : self.amount_of_burners,
                "bread_basket" : self.bread_basket,
                "amount_of_wheels" : self.amount_of_wheels,
                "length_in_cm" : self.length_in_cm,
                "width_in_cm" : self.width_in_cm,
                "product_price": self.product_price
                }