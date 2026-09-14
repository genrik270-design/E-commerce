import pytest
from src.BaseGroup import BaseGroup
from src.Category import Category
from src.Order import Order
from src.Product import Product


def test_base_group_abstract():
    """Проверяем, что нельзя создать экземпляр абстрактного класса BaseGroup напрямую."""
    with pytest.raises(TypeError):
        BaseGroup()


def test_order_creation_and_calculation(capsys):
    """Проверяем успешное создание заказа, подсчет стоимости, работу len() и миксина."""
    # Создаем тестовый продукт
    product = Product("Тестовый смартфон", "Описание", 50000.0, 10)

    # Сбрасываем перехваченный миксином принт от создания продукта
    capsys.readouterr()

    # Фиксируем начальное количество заказов
    initial_count = Order.order_count

    # Создаем заказ на 3 единицы товара
    order = Order(product, 3)

    # 1. Проверяем расчет стоимости
    assert order.total_cost == 150000.0

    # 2. Проверяем работу метода __len__ (должен возвращать количество товара)
    assert len(order) == 3

    # 3. Проверяем счетчик заказов
    assert Order.order_count == initial_count + 1

    # 4. Проверяем, что миксин отработал и для заказа
    captured = capsys.readouterr()
    assert "Order" in captured.out
    assert "Тестовый смартфон" in captured.out


def test_category_len_with_base_group():
    """Проверяем, что метод len() корректно работает для Категории через новый абстрактный класс."""
    product1 = Product("Товар 1", "Описание 1", 100.0, 5)
    product2 = Product("Товар 2", "Описание 2", 200.0, 10)

    category = Category("Электроника", "Гаджеты", [product1, product2])

    # Проверяем, что len() возвращает количество уникальных продуктов в категории
    assert len(category) == 2
