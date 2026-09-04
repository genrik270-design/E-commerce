from src.Category import Category


def test_category_init(sample_category):
    """Проверка корректности инициализации объекта класса Category."""
    assert sample_category.name == "Смартфоны"
    assert sample_category.description == "Различные смартфоны"
    assert len(sample_category.products.split("\n")) == 3

def test_category_counters(sample_category):
    """Проверка подсчета общего количества категорий и уникальных товаров."""
    assert Category.category_count == 1
    assert Category.product_count == 2
