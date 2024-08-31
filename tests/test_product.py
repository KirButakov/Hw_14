import pytest

from src.product import Product


def test_product_creation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_str():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    assert str(product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_price_setter():
    product = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    product.price = 35000.0
    assert product.price == 35000.0
    with pytest.raises(ValueError):
        product.price = -1000.0


def test_product_addition():
    product1 = Product("Product1", "Description1", 100.0, 5)
    product2 = Product("Product2", "Description2", 150.0, 3)
    assert product1 + product2 == 100 * 5 + 150 * 3
    with pytest.raises(TypeError):
        product1 + "NotAProduct"


def test_product_new_product():
    product_info = {"name": "New Product", "description": "New Description", "price": 500.0, "quantity": 10}
    product = Product.new_product(product_info)
    assert product.name == "New Product"
    assert product.description == "New Description"
    assert product.price == 500.0
    assert product.quantity == 10
