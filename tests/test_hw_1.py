from src.category import Category
from src.product import Product


def test_product_initialization():
    product = Product("Product1", "Description1", 100.0, 10)
    assert product.name == "Product1"
    assert product.description == "Description1"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    category = Category("Category1", "Description1")
    assert category.name == "Category1"
    assert category.description == "Description1"
    assert len(category.products) == 0


def test_add_product_to_category():
    category = Category("Category1", "Description1")
    product = Product("Product1", "Description1", 100.0, 10)
    category.add_product(product)
    assert len(category.products) == 1
    assert category.products[0] == product


def test_total_categories_and_products():
    # Reset class-level counters before the test
    Category.total_categories = 0
    Category.total_products = 0

    category1 = Category("Category1", "Description1", [])
    category2 = Category("Category2", "Description2", [])

    assert Category.total_categories == 2

    product1 = Product("Product1", "Description1", 100.0, 10)
    product2 = Product("Product2", "Description2", 150.0, 5)

    category1.add_product(product1)
    category2.add_product(product2)

    assert Category.total_products == 2


def test_category_with_initial_products():
    product1 = Product("Product1", "Description1", 100.0, 10)
    product2 = Product("Product2", "Description2", 150.0, 5)

    category = Category("Category1", "Description1", [product1, product2])

    assert category.name == "Category1"
    assert category.description == "Description1"
    assert len(category.products) == 2
    assert category.products[0] == product1
    assert category.products[1] == product2
    assert Category.total_products == 2
