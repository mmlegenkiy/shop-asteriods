from shop_exceptions import ShopException

class NotNegativeValue:
    def __set_name__(self, owner, name):
        self._attr_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._attr_name, 0)

    def __set__(self, instance, value):
        if type(value) is int and value >= 0:
            setattr(instance, self._attr_name, value)
        else:
            raise ShopException(f"Not valid {self._attr_name} value")


class Product:

    """Клас товар. Товар може бути зарезервований - доданий до корзини."""

    amount = NotNegativeValue()
    reserved = NotNegativeValue()

    def __init__(self, title, price, amount):
        self.title = title
        self.price = price
        self.amount = amount
        self.reserved = 0

    def reserve(self, amount):
        """Додати до резерву (корзини) відповідну кількість товару"""
        if amount <= self.amount:
            self.amount -= amount
            self.reserved += amount
        else:
            raise ShopException(f"Try to reserve more {self.title} than is available")

    def unreserve(self, amount):
        """Прибрати із резерву (корзини) відповідну кількість товару"""
        if self.reserved >= amount:
            self.amount += amount
            self.reserved -= amount
        else:
            raise ShopException(f"Try to unreserve not reserved product")

    def take_from_reserve(self, amount):
        """Прибрати із резерву (корзини) відповідну кількість товару і додати до замовлення"""
        if self.reserved >= amount:
            self.reserved -= amount
        else:
            raise ShopException(f"Try to unreserve not reserved product")
