class Category:
    total_categories = 0
    total_products = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []
        Category.total_categories += 1
        Category.total_products += len(self.products)

    @property
    def category_count(self):
        return Category.total_categories

    @property
    def product_count(self):
        return Category.total_products

    def add_product(self, product):
        self.products.append(product)
        Category.total_products += 1
