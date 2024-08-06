from product_2 import Product


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]

    def add_product(self, product):
        if isinstance(product, Product):
            self._products.append(product)

    @property
    def product_count(self):
        return len(self._products)
