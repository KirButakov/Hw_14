from src.category import Category
from src.product import Product


def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.product_count == 2


def test_category_add_product():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    category = Category("Test Category", "Test Description")
    assert category.product_count == 0
    category.add_product(product1)
    assert category.product_count == 1


def test_category_products_property():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    products = category.products
    assert products == ["Product 1, 100.0 руб. Остаток: 10 шт.", "Product 2, 200.0 руб. Остаток: 20 шт."]


def test_category_str():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert str(category) == "Test Category, количество продуктов: 30 шт."
