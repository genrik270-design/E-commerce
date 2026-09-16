import pytest
from src.Category import Category
from src.Product import Product


def test_category_init(sample_category):
    """Проверка корректности инициализации объекта класса Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Различные смартфоны"
    assert len(sample_category.products.split("\n")) == 3


def test_category_counters(sample_category):
    """Проверка подсчета общего количества категорий и уникальных товаров."""
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_category_average_price():
    """Тест: Проверяем корректный расчет средней цены, когда товары есть."""
    p1 = Product("Товар 1", "Описание 1", 100.0, 5)
    p2 = Product("Товар 2", "Описание 2", 200.0, 10)

    category = Category("Продукты", "Еда", [p1, p2])
    # Средняя цена между 100 и 200 должна быть 150
    assert category.average_price() == 150.0


def test_category_average_price_with_empty_list():
    """Тест: Проверяем, что для пустой категории исключение возвращает 0.0."""
    empty_category = Category("Пустая категория", "Описания нет", [])

    # Метод должен отработать через except и вернуть 0.0 без падения программы
    assert empty_category.average_price() == 0.0


def test_add_product_success_messages(capsys):
    """Тест проверяет вывод сообщений из блоков else и finally при успехе."""
    p = Product("Тестовый телефон", "Описание", 10000.0, 5)
    category = Category("Тест", "Описание", [])

    # Сбрасываем старые принты от создания объектов
    capsys.readouterr()

    # Вызываем добавление
    category.add_product(p)

    # Читаем то, что напечатал метод add_product
    captured = capsys.readouterr()

    # Проверяем наличие фраз из else и finally
    assert "успешно добавлен" in captured.out
    assert "Обработка добавления товара завершена." in captured.out


def test_add_product_error_finally_message(capsys):
    """Тест проверяет, что блок finally выполняется даже при ошибке типа товара."""
    category = Category("Тест", "Описание", [])
    capsys.readouterr()

    # Пытаемся добавить строку вместо объекта Product (вызовет TypeError)
    with pytest.raises(TypeError):
        category.add_product("Не товар")

    captured = capsys.readouterr()

    # Блок finally обязан выполниться в 100% случаев
    assert "Обработка добавления товара завершена." in captured.out
