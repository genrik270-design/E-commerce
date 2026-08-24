import pytest
from src.Category import Category
from src.Product import Product


@pytest.fixture
def product_iphone():
    """Фикстура для тестирования 1-го продукта"""
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def sample_category(product_iphone):
    """Фикстура для тестирования категории."""
    # Сбрасываем счетчики класса, чтобы тесты не зависели друг от друга
    Category.category_count = 0
    Category.product_count = 0
    product_samsung = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5
    )
    return Category(
        "Смартфоны", "Различные смартфоны", [product_iphone, product_samsung]
    )
