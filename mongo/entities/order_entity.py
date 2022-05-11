class Order_entity:
    def __init__(self, user_id, order_id, product):
        self.user_id = user_id,
        self.order_id = order_id,
        self.product = product 


    def return_order(self):
        return {"user_id": self.user_id, 
                "order_id": self.order_id,
                "product": self.product
                }