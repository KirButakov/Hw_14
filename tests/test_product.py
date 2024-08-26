import pytest

from src.product import LawnGrass, Product, Smartphone


def test_product_initialization():
    product = Product("Товар", "Описание товара", 100.0, 10)
    assert product.name == "Товар"
    assert product.price == 100.0
    assert product.quantity == 10


def test_smartphone_initialization():
    smartphone = Smartphone("iPhone", "Описание iPhone", 50000, 5, 98.5, "iPhone 12", 128, "Black")
    assert smartphone.name == "iPhone"
    assert smartphone.efficiency == 98.5
    assert smartphone.model == "iPhone 12"


def test_lawn_grass_initialization():
    grass = LawnGrass("Газонная трава", "Описание травы", 500, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"


def test_add_same_type_products():
    smartphone1 = Smartphone("Samsung", "Описание", 1000, 2, 95, "S23", 256, "Gray")
    smartphone2 = Smartphone("iPhone", "Описание", 2000, 1, 98, "12", 512, "Black")
    total_value = smartphone1 + smartphone2
    assert total_value == 4000  # 1000*2 + 2000*1


def test_add_different_type_products_raises_typeerror():
    smartphone = Smartphone("Samsung", "Описание", 1000, 2, 95, "S23", 256, "Gray")
    grass = LawnGrass("Газонная трава", "Описание", 500, 20, "Россия", "7 дней", "Зеленый")

    with pytest.raises(TypeError):
        result = smartphone + grass
