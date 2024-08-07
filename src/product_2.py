class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative")
        else:
            self._price = value

    @classmethod
    def new_product(cls, product_info):
        return cls(product_info["name"], product_info["description"], product_info["price"], product_info["quantity"])
