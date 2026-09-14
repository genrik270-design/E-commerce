from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self):
        """Обязательный метод вывода строки для наследников."""
        pass

    @classmethod
    @abstractmethod
    def create_product(cls, *args, **kwargs):
        """Метод создания продукта."""
        pass
