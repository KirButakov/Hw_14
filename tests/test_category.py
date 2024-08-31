from src.category import Category
from src.product import Product


def test_category_creation():
    product1 = Product("Product1", "Description1", 100.0, 10)
    product2 = Product("Product2", "Description2", 200.0, 5)
    category = Category("Electronics", "All electronic items", [product1, product2])
    assert category.name == "Electronics"
    assert category.description == "All electronic items"
    assert category.product_count == 2
    assert len(category.products) == 2


def test_add_product_to_category():
    product = Product("Product3", "Description3", 150.0, 7)
    category = Category("Furniture", "All furniture items")
    category.add_product(product)
    assert category.product_count == 1
    assert category.products == ["Product3, 150.0 руб. Остаток: 7 шт."]


def test_category_count():
    Category.category_count = 0  # Reset for testing
    product1 = Product("Product4", "Description4", 250.0, 4)
    product2 = Product("Product5", "Description5", 500.0, 2)
    category1 = Category("Appliances", "Home appliances", [product1])
    category2 = Category("Decor", "Home decor", [product2])
    assert Category.category_count == 2


def test_total_product_count():
    Category.total_product_count = 0  # Reset for testing
    product1 = Product("Product6", "Description6", 350.0, 6)
    category = Category("Tools", "Various tools", [product1])
    assert Category.total_product_count == 1
    product2 = Product("Product7", "Description7", 450.0, 3)
    category.add_product(product2)
    assert Category.total_product_count == 2
