from src.BaseGroup import BaseGroup
from src.Product import Product
from src.PrintMixin import PrintMixin


class Order(PrintMixin, BaseGroup):
    """Класс, представляющий заказ на один определенный товар."""

    order_count = 0  # Счетчик всех созданных заказов

    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity
        # Автоматически вычисляем итоговую стоимость заказа
        self.total_cost = product.price * quantity

        # Увеличиваем общий счетчик заказов в системе
        Order.order_count += 1

        # Вызываем super() для цепочки миксина
        super().__init__()

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Стоимость: {self.total_cost} руб."

    def __len__(self) -> int:
        """В заказе количество элементов — это количество купленного товара."""
        return self.quantity
