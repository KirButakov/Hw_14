# My Homework

## Описание
Этот проект демонстрирует реализацию классов для продуктов и категорий, а также их тестирование с использованием pytest.

## Установка
poetry install

## Запуск тестов
pytest

## Структура проекта
- src/: исходные коды
- tests/: тесты

## Новый функционал

- Приватный атрибут списка товаров в классе `Category`.
- Метод `add_product` для добавления товаров в категорию.
- Класс-метод `new_product` для создания нового товара из словаря.

### Класс Product
- Метод `__str__`: Возвращает строку в формате "Название продукта, цена руб. Остаток: количество шт."
- Метод `__add__`: Возвращает общую стоимость всех товаров на складе при сложении двух продуктов.

### Класс Category
- Метод `__str__`: Возвращает строку в формате "Название категории, количество продуктов: общее количество шт."

## Новый функционал

Добавлены классы-наследники `Smartphone` и `LawnGrass` для категории товаров. 
Реализован метод сложения для продуктов одного типа и защита от сложения продуктов разных типов.
Обновлен метод добавления продукта в категорию с проверкой типа объекта.



