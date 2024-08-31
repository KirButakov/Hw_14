class Category_2:
    def __init__(self, name, products=None):
        self.name = name
        self.products = products if products is not None else []

    def average_price(self):
        try:
            total_price = sum(product._price for product in self.products)
            count = len(self.products)
            if count == 0:
                return 0
            return total_price / count
        except ZeroDivisionError:
            return 0
