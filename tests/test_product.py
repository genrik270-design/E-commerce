from src.Product import Product


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

    product = Product.new_product(product_data)

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
