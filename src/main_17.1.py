from src.category_2 import Category_2
from src.product_2 import Product_2

if __name__ == "__main__":
    try:
        product_invalid = Product_2("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    product1 = Product_2("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product_2("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product_2("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category_2("Смартфоны", [product1, product2, product3])

    print(round(category1.average_price(), 2))

    category_empty = Category_2("Пустая категория", [])
    print(round(category_empty.average_price(), 2))
