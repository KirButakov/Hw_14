import pytest

from src.category import Category


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.total_categories = 0
    Category.total_products = 0
