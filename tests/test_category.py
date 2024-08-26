import pytest

from src.category import Category
from src.product import Smartphone


def test_category_initialization():
    category = Category("Смартфоны", "Категория смартфонов")
    assert category.name == "Смартфоны"
    assert category.description == "Категория смартфонов"
    assert category.product_count == 0


def test_add_product_to_category():
    category = Category("Смартфоны", "Категория смартфонов")
    smartphone = Smartphone("iPhone", "Описание iPhone", 50000, 5, 98.5, "iPhone 12", 128, "Black")
    category.add_product(smartphone)
    assert category.product_count == 1


def test_add_invalid_product_raises_typeerror():
    category = Category("Смартфоны", "Категория смартфонов")

    with pytest.raises(TypeError):
        category.add_product("Not a product")
