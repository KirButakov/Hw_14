class Category:
    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self._products = products

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products(self):
        return [str(product) for product in self._products]
