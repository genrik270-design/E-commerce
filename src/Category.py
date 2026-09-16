from src.BaseGroup import BaseGroup
from src.PrintMixin import PrintMixin
from src.exceptions import ZeroQuantityError


class Category(PrintMixin, BaseGroup):
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
        super().__init__()

    def __len__(self) -> int:
        """Возвращает количество продуктов в категории."""
        return len(self.__products)

    def __str__(self):
        # Считаем сумму штук всех товаров в категории
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    # Геттер для получения списка товаров в нужном формате
    @property
    def products(self) -> str:
        # Превращаем каждый объект продукта в строку благодаря нашему Product.__str__
        return "".join([f"{str(p)}\n" for p in self.__products])

    def average_price(self) -> float:
        """Подсчитывает средний ценник всех товаров в категории.
        С помощью исключений обрабатывает случай, когда в категории нет товаров.
        """
        try:
            total_sum = sum(product.price for product in self.__products)
            return total_sum / len(self.__products)
        except ZeroDivisionError:
            return 0.0

    # Метод для добавления товара (теперь он внутри класса)
    def add_product(self, product):
        """Добавляет продукт в категорию с проверкой его типа."""
        from src.Product import Product  # Импортируем внутри метода во избежание циклического импорта

        try:
            # 1. Проверяем, является ли объект экземпляром класса Product или его наследников
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников!")

            # 2. Проверяем количество товара
            if product.quantity == 0:
                raise ZeroQuantityError()

                # Если проверки прошли, добавляем в список
            self.__products.append(product)
            Category.product_count += 1

        except (TypeError, ZeroQuantityError) as e:
            # Отступ блока except должен быть ровно 4 пробела от левого края (на уровне с def)
            print(f"Ошибка добавления: {e}")
            raise

        else:
            # Отступ ровно 4 пробела от левого края
            print(f"Товар '{product.name}' успешно добавлен.")

        finally:
            # Отступ ровно 4 пробела от левого края
            print("Обработка добавления товара завершена.")
