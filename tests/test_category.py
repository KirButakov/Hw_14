from src.category import Category
from src.product import Product


def test_category_creation():
    product1 = Product("Product1", "Description1", 100.0, 5)
    product2 = Product("Product2", "Description2", 150.0, 3)
    category = Category("Category1", "Description of Category1", [product1, product2])

    assert category.name == "Category1"
    assert category.description == "Description of Category1"
    assert category.product_count == 2
    assert Category.get_category_count() == 1
    assert Category.get_total_product_count() == 2


def test_category_add_product():
    product = Product("Product3", "Description3", 200.0, 7)
    category = Category("Category2", "Description of Category2")
    category.add_product(product)

    assert category.product_count == 1
    assert Category.get_total_product_count() == 3


def test_category_products_property():
    product1 = Product("Product1", "Description1", 100.0, 5)
    product2 = Product("Product2", "Description2", 150.0, 3)
    category = Category("Category3", "Description of Category3", [product1, product2])

    expected_products = ["Product1, 100.0 руб. Остаток: 5 шт.", "Product2, 150.0 руб. Остаток: 3 шт."]
    assert category.products == expected_products


def test_category_str():
    product1 = Product("Product1", "Description1", 100.0, 5)
    product2 = Product("Product2", "Description2", 150.0, 3)
    category = Category("Category4", "Description of Category4", [product1, product2])

    assert str(category) == "Category4, количество продуктов: 8 шт."
