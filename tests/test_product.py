import pytest
from src.Product import Product, Smartphone, LawnGrass
from src.BaseProduct import BaseProduct


def test_product_init(product_iphone):
    """Проверка корректности инициализации объекта класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_new_product():
    """Проверка создания объекта Product через класс-метод."""
    # Создаем словарь с данными продукта
    product_data = {
        "name": "Sony PlayStation 5",
        "description": "Игровая консоль, 825GB",
        "price": 60000.0,
        "quantity": 3
    }

    product = Product.create_product(product_data)

    # Добавьте проверки (assert), если их еще нет
    assert product.name == "Sony PlayStation 5"
    assert product.price == 60000.0
    assert product.quantity == 3


def test_product_price_setter_invalid(capsys):
    """Проверка, что отрицательная цена не устанавливается и выводится сообщение."""
    product = Product("Тестовый товар", "Описание", 100.0, 10)

    # Пытаемся поставить некорректную цену
    product.price = -10.0

    # Проверяем, что цена НЕ изменилась
    assert product.price == 100.0

    # Проверяем, что в консоль вывелся нужный текст
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_product_price_decrease_reject(monkeypatch, capsys):
    """Проверка отмены снижения цены, если пользователь ввел 'n'."""
    import sys
    product = Product("Товар", "Описание", 100.0, 10)

    monkeypatch.delitem(sys.modules, "pytest", raising=False)
    monkeypatch.setattr('builtins.input', lambda _: "n")

    product.price = 50.0  # Пытаемся снизить цену

    assert product.price == 100.0  # Цена не должна измениться
    captured = capsys.readouterr()
    assert "Операция отменена" in captured.out


def test_product_price_decrease_accept(monkeypatch):
    """Проверка успешного снижения цены при согласии пользователя."""
    import sys
    product = Product("Товар", "Описание", 100.0, 10)

    # Имитируем ручной запуск и ввод 'y' (согласие)
    monkeypatch.delitem(sys.modules, "pytest", raising=False)
    monkeypatch.setattr('builtins.input', lambda _: "y")

    product.price = 80.0  # Снижаем цену
    assert product.price == 80.0  # Цена ДОЛЖНА измениться


def test_smartphone_init():
    """ Тестируем инициализацию смартфона"""
    phone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")

    # Проверяем базовые свойства
    assert phone.name == "Iphone 15"
    assert phone.price == 210000.0
    assert phone.quantity == 8
    # Проверяем уникальные свойства смартфона
    assert phone.efficiency == 98.2
    assert phone.model == "15"
    assert phone.memory == 512
    assert phone.color == "Gray space"


def test_lawn_grass_init():
    """Тест корректной инициализации газонной травы."""
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 7, "Зеленый")

    # Проверяем базовые свойства
    assert grass.name == "Газонная трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    # Проверяем уникальные свойства травы
    assert grass.country == "Россия"
    assert grass.germination_period == 7
    assert grass.color == "Зеленый"


def test_products_add_success():
    """Тест успешного сложения товаров ОДНОГО класса."""
    phone1 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    phone2 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")
    # Ожидаем: (210000 * 8) + (31000 * 14) = 1680000 + 434000 = 2114000
    assert phone1 + phone2 == 2114_000


def test_products_add_type_error():
    """Тест ошибки при сложении товаров РАЗНЫХ классов."""
    phone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    grass = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", 7, "Зеленый")

    # Проверяем, что генерируется ошибка TypeError при сложении смартфона и травы
    with pytest.raises(TypeError):
        phone + grass


def test_base_product_abstract():
    """Проверяем, что нельзя создать экземпляр абстрактного класса BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 1)


def test_product_creation_with_mixin(capsys):
    """Проверяем, что при создании продукта миксин выводит информацию в консоль."""
    # Создаем продукт. capsys перехватывает все принты
    Product("Sony PlayStation 5", "Игровая консоль", 60000.0, 3)

    # Читаем вывод в консоль
    captured = capsys.readouterr()

    # Проверяем, что в выводе присутствует имя класса и ключевые параметры
    assert "Product" in captured.out
    assert "Sony PlayStation 5" in captured.out
    assert "60000.0" in captured.out
    assert "3" in captured.out


def test_create_product_factory():
    """Проверяем фабричный метод создания продукта из словаря."""
    product_data = {
        "name": "Sony PlayStation 5",
        "description": "Игровая консоль, 825GB",
        "price": 60000.0,
        "quantity": 3
    }

    # ВАЖНО: Используйте то имя метода, которое у вас осталось в коде (create_product или new_product)
    product = Product.create_product(product_data)

    assert product.name == "Sony PlayStation 5"
    assert product.price == 60000.0
    assert product.quantity == 3
