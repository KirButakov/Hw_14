import pytest

from src.product_2 import Product_2


def test_product_creation_valid():
    product = Product_2("Valid Product", "Description", 100.0, 5)
    assert product.name == "Valid Product"
    assert product.description == "Description"
    assert product._price == 100.0
    assert product.quantity == 5


def test_product_creation_invalid_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product_2("Invalid Product", "Description", 100.0, 0)
