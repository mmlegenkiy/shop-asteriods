from shop_exceptions import ShopException

class NotNegativeValue:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if type(value) is int and value >= 0:
            instance.__dict__[self.name] = value
        else:
            raise ShopException(f'{self.name.capitalize()} must be not negative integer value!')


class Product:

    """Клас товар. Товар може бути зарезервований - доданий до корзини."""

    amount = NotNegativeValue()
    # reserved = NotNegativeValue()

    def __init__(self, item_id, title, price, amount):
        self.item_id = item_id
        self.title = title
        self.price = price
        self.amount = amount

    def __repr__(self):
        return f'id: {self.item_id}, {self.title}, price: {self.price}, amount: {self.amount}'

    def take(self, amount):
        """Додати до резерву (корзини) відповідну кількість товару"""
        self.amount -= amount

    def add(self, amount):
        """Додати до резерву (корзини) відповідну кількість товару"""
        self.amount += amount
