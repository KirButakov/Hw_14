from src.category_2 import Category_2
from src.product_2 import Product_2


def test_category_creation_with_products():
    product1 = Product_2("Product 1", "Description 1", 100.0, 5)
    product2 = Product_2("Product 2", "Description 2", 200.0, 10)
    category = Category_2("Category 1", [product1, product2])

    assert category.name == "Category 1"
    assert len(category.products) == 2


def test_category_average_price_with_products():
    product1 = Product_2("Product 1", "Description 1", 100.0, 5)
    product2 = Product_2("Product 2", "Description 2", 200.0, 10)
    category = Category_2("Category 1", [product1, product2])

    assert category.average_price() == 150.0  # (100 + 200) / 2


def test_category_average_price_empty():
    category = Category_2("Empty Category", [])
    assert category.average_price() == 0


def test_category_average_price_with_one_product():
    product = Product_2("Single Product", "Description", 300.0, 1)
    category = Category_2("Single Product Category", [product])

    assert category.average_price() == 300.0
