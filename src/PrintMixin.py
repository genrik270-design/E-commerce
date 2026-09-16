class PrintMixin:
    """Миксин для логирования создания объекта через __repr__."""

    def __init__(self, *args, **kwargs):
        # Сначала передаем управление дальше по цепочке (в Product -> BaseProduct),
        # чтобы объект полностью создался и у него появились все атрибуты
        super().__init__(*args, **kwargs)

        print(repr(self))

    def __repr__(self) -> str:
        """Рекомендованная реализация отладочного вывода.
        Собирает имя класса и все его текущие свойства."""
        # Собираем свойства в формате "ключ=значение" (строки оборачиваем в кавычки через repr)
        props = [f"{key}={repr(value)}" for key, value in self.__dict__.items() if not key.startswith('_')]

        # Если есть приватные или защищенные переменные (например, _price),
        # приводим их имя к красивому виду 'price' для репрезентативности
        for key, value in self.__dict__.items():
            if key.startswith('_') and not key.startswith('__'):
                clean_key = key.lstrip('_')
                props.append(f"{clean_key}={repr(value)}")

        return f"{self.__class__.__name__}({', '.join(props)})"
