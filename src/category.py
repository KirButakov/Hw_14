from src.product import Product


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self._products = products if products is not None else []

    @property
    def products(self):
        return [f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт." for product in self._products]

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self._products.append(product)
        else:
            raise TypeError("Можно добавлять только объекты класса Product и его наследников")

    @property
    def product_count(self):
        return len(self._products)

    def __str__(self):
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."
