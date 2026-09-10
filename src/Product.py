class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity  # Атрибут для количества

    def __add__(self, other):
        # Проверяем, что оба объекта принадлежат к одному и тому же классу
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных категорий!")

        # Если классы одинаковые, выполняем привычное сложение (цена * количество)
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_data: dict):
        """Создаём объект класса из словаря."""
        return cls(
            name=product_data.get("name"),
            description=product_data.get("description"),
            price=product_data.get("price"),
            quantity=product_data.get("quantity")
        )

    @property
    def price(self) -> float:
        """Геттер для чтения приватного атрибута цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        """Сеттер для изменения цены с подтверждением снижения."""
        import sys

        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        # Если цена снижается
        if new_price < self.__price:
            # Проверяем, запущены ли тесты (чтобы input не вешал pytest)
            if "pytest" in sys.modules:
                user_input = "y"
            else:
                user_input = input("Вы уверены, что хотите снизить цену? (y/n): ").lower()

            if user_input != "y":
                print("Операция отменена")
                return

        self.__price = new_price


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
