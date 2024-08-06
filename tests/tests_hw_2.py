import pytest

from src.category_2 import Category
from src.product_2 import Product


def test_product_initialization():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_price_setter():
    product = Product("Test Product", "Test Description", 100.0, 10)
    product.price = 200.0
    assert product.price == 200.0

    with pytest.raises(ValueError):
        product.price = -100.0

    product.price = 0
    assert product.price == 0.0


def test_product_new_product_class_method():
    product_info = {"name": "Test Product", "description": "Test Description", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_info)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_category_initialization():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    assert category.name == "Test Category"
    assert category.description == "Test Description"
    assert category.product_count == 2


def test_category_add_product():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1])
    assert category.product_count == 1
    category.add_product(product2)
    assert category.product_count == 2
    assert len(category.products) == 2


def test_category_products_property():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    category = Category("Test Category", "Test Description", [product1, product2])
    products = category.products
    assert products == ["Product 1, 100.0 руб. Остаток: 10 шт.", "Product 2, 200.0 руб. Остаток: 20 шт."]
