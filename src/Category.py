class Category:
    # Атрибуты класса для подсчета количества
    category_count = 0  # Общее количество категорий
    product_count = 0  # Количество уникальных товаров

    def __init__(self, name: str, description: str, products: list = None):
        self.name = name
        self.description = description

        # Переводим в приватный режим (два подчеркивания)
        self.__products = []

        # При создании новой категории увеличиваем счетчик категорий на 1
        Category.category_count += 1

        # Если список продуктов передан, добавляем их через метод add_product
        if products is not None:
            for product in products:
                self.add_product(product)

    # Геттер для получения списка товаров в нужном формате
    @property
    def products(self) -> str:
        return "".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n" for p in self.__products])

    # Метод для добавления товара (теперь он внутри класса)
    def add_product(self, product):
        self.__products.append(product)  # Добавление через append
        Category.product_count += 1  # Увеличение счетчика
