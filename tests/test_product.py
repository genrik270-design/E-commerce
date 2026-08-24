def test_product_init(product_iphone):
    """Проверка корректности инициализации объекта класса Product."""
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8
