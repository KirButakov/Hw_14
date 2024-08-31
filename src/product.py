from abc import ABC, abstractmethod


# Абстрактный класс
class BaseProduct(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_price(self):
        pass


# Миксин для логирования
class LogMixin:
    def __init__(self):
        class_name = self.__class__.__name__
        print(f"Создан объект класса {class_name} с параметрами: {self.__dict__}")


# Класс Product
class Product(LogMixin, BaseProduct):
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        super().__init__()  # Вызов конструктора LogMixin без аргументов

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self._price = value

    @classmethod
    def new_product(cls, product_info):
        return cls(product_info["name"], product_info["description"], product_info["price"], product_info["quantity"])

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        raise TypeError("Нельзя сложить продукты разных типов")

    def get_info(self):
        return f"{self.name}: {self.description}"

    def get_price(self):
        return self._price


# Подкласс Smartphone
class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_info(self):
        return f"{self.name} - {self.model}: {self.description}"


# Подкласс LawnGrass
class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        return f"{self.name} ({self.color}) - {self.description}"
