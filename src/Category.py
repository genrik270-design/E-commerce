class Category:
    # Атрибуты класса для подсчета количества
    category_count = 0  # Общее количество категорий
    product_count = 0  # Количество уникальных товаров

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

        # При создании новой категории увеличиваем счетчик категорий на 1
        Category.category_count += 1

        # Увеличиваем счетчик уникальных товаров на количество элементов в списке
        Category.product_count += len(self.products)
