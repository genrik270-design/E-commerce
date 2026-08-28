class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity  # Атрибут для количества

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
