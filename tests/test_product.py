import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_creation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 200000.0
    assert product.price == 200000.0
    with pytest.raises(ValueError):
        product.price = -100.0


def test_product_addition():
    product1 = Product("Product1", "Description1", 100.0, 10)
    product2 = Product("Product2", "Description2", 200.0, 5)
    total_value = product1 + product2
    assert total_value == 1000.0  # (100 * 10) + (200 * 5)


def test_smartphone_creation():
    smartphone = Smartphone("Samsung Galaxy S23", "Smartphone", 150000.0, 3, "High", "S23", "128GB", "Black")
    assert smartphone.name == "Samsung Galaxy S23"
    assert smartphone.efficiency == "High"
    assert smartphone.memory == "128GB"


def test_lawn_grass_creation():
    lawn_grass = LawnGrass("Luxury Grass", "Premium quality", 3000.0, 20, "USA", "2 weeks", "Green")
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == "2 weeks"
