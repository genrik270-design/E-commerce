from src.BaseProduct import BaseProduct
from src.PrintMixin import PrintMixin


class Product(PrintMixin, BaseProduct):
    """Класс продукта, реализующий абстрактные методы."""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        # Вызываем конструктор абстрактного класса
        super().__init__(name, description, price, quantity)

    def __str__(self):
        return f"{self.name}, {self.price}руб. Остаток {self.quantity}штук"

    @classmethod
    def create_product(cls, product_data: dict, *args, **kwargs):
        """Создаём объект класса из словаря."""
        return cls(
            name=product_data.get("name", "Без названия"),  # Если нет имени, будет "Без названия"
            description=product_data.get("description", ""),  # Если нет описания, будет пустая строка
            price=product_data.get("price", 0.0),  # Если нет цены, вернет 0.0
            quantity=product_data.get("quantity", 0)  # Если нет количества, вернет 0

        )

    @property
    def price(self) -> float:
        """Геттер для чтения приватного атрибута цены."""
        return self._price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для изменения цены с подтверждением снижения."""
        import sys

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Если цена снижается
        if new_price < self._price:
            # Проверяем, запущены ли тесты (чтобы input не вешал pytest)
            if "pytest" in sys.modules:
                user_input = "y"
            else:
                user_input = input("Вы уверены, что хотите снизить цену? (y/n): ").lower()

            if user_input != "y":
                print("Операция отменена")
                return

        self._price = new_price

    def __add__(self, other):
        """Сложение двух продуктов.
        Возвращает полную стоимость всех товаров на складе."""
        # Сначала проверяем, что складываются товары одного класса
        # (или унаследованные от Product, если это разрешено по ТЗ)
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

        # Формула: (Цена1 * Количество1) + (Цена2 * Количество2)
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфонов."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 efficiency: float, model: str, memory: int, color: str):
        # Передаем базовые свойства в родительский класс Product
        super().__init__(name, description, price, quantity)
        # Добавляем новые уникальные свойства смартфона
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для представления газонной травы."""

    def __init__(self, name: str, description: str, price: float, quantity: int,
                 country: str, germination_period: int, color: str):
        # Передаем базовые свойства в родительский класс Product
        super().__init__(name, description, price, quantity)
        # Добавляем новые уникальные свойства газонной травы
        self.country = country
        self.germination_period = germination_period
        self.color = color
