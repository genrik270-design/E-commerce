class ProductIterator:
    def __init__(self, category_obj):
        """Сохраняем ссылку на объект категории и задаем начальный индекс."""
        self.category = category_obj
        self.index = 0

    def __iter__(self):
        """Возвращает сам объект итератора для начала цикла."""
        return self

    def __next__(self):
        """Возвращает следующий товар из категории на каждом шаге цикла."""
        # Получаем доступ к приватному списку продуктов через Name Mangling
        products_list = self.category._Category__products

        # Проверяем, есть ли ещё товары для перебора
        if self.index < len(products_list):
            product = products_list[self.index]
            self.index += 1
            return product
        else:
            # Прекращаем цикл, когда товары закончились
            raise StopIteration
