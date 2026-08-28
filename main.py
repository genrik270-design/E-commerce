import json
from src.Category import Category
from src.Product import Product


def load_data(file_path: str) -> list[Category]:
    """Читает файл JSON и создает объекты классов Category и Product."""
    categories = []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)  # Загружаем сырые данные из JSON

    for category_data in data:
        products_list = []

        # Сначала собираем объекты товаров для текущей категории
        for product_data in category_data.get("products", []):
            product = Product(
                name=product_data["name"],
                description=product_data["description"],
                price=product_data["price"],
                quantity=product_data["quantity"],
            )
            products_list.append(product)

        # Затем создаем саму категорию и передаем туда готовый список товаров
        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products_list,
        )
        categories.append(category)

    return categories


# --- Пример использования в main.py ---
if __name__ == "__main__":
    # Указываем путь к файлу products.json относительно корня проекта
    loaded_categories = load_data("products.json")

    # Проверяем, что объекты создались корректно
    print(f"Всего подгружено категорий: {Category.category_count}")
    print(f"Всего подгружено уникальных товаров: {Category.product_count}")

    print("\n--- Список категорий и товаров ---")
    for cat in loaded_categories:
        print(f"\nКатегория: {cat.name} ({cat.description})")
        print("Товары:")
        print(cat.products)

if __name__ == "__main__":
    Category.category_count = 0
    Category.product_count = 0
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")  # Выведет: True
    print(category1.description)
    print(category1.product_count)  # Выведет: 3
    print(category1.category_count)  # Выведет: 1
    print(category1.product_count)  # Выведет: 3

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(Category.category_count)  # Выведет: 2
    print(Category.product_count)  # Выведет: 4

    print(category1.products)

    product5 = Product.new_product({
        "name": "Sony PlayStation 5",
        "description": "Игровая консоль",
        "price": 60000.0,
        "quantity": 3
    })

    print(f"{product5.name}, {product5.price} руб. Остаток: {product5.quantity} шт.")
