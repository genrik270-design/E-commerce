from abc import ABC, abstractmethod


class BaseGroup(ABC):
    """Абстрактный класс для группирующих сущностей (Категории, Заказы)."""

    @abstractmethod
    def __init__(self):
        """Конструктор обязателен, чтобы цепочка super().__init__() работала корректно."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Обязательный строковый вывод."""
        pass

    @abstractmethod
    def __len__(self) -> int:
        """Возвращает количество элементов (продуктов) внутри группы."""
        pass
