import pytest

from src.product import Product


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


def test_product_new_product_class_method():
    product_info = {"name": "Test Product", "description": "Test Description", "price": 100.0, "quantity": 10}
    product = Product.new_product(product_info)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert str(product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_add():
    product1 = Product("Product 1", "Description 1", 100.0, 10)
    product2 = Product("Product 2", "Description 2", 200.0, 20)
    assert product1 + product2 == 5000.0  # 100.0*10 + 200.0*20
