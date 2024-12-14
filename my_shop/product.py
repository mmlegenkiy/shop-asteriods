from shop_exceptions import ShopException


class NotNegativeValue:
    """
    Клас-дескриптор для створення не негативних цілих значень.
    Завдяки використанню цього класу повинно контролюватися, що відповідний
    атрибут не набуває від'ємних значень, отже користувач не може додати
    до корзини більшу кількість товару ніж є доступним
    """
    def __set_name__(self, owner, name):
        """
        Магічний метод, де задається назва атрибута
        """
        self.name = name

    def __get__(self, instance, owner):
        """
        Магічний метод, що повертає значення атрибута
        """
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        """
        Магічний метод, що встановлює значення атрибута.
        Якщо встановлюється неціле або від'ємне значення,
        то генерується виняток
        """
        if type(value) is int and value >= 0:
            instance.__dict__[self.name] = value
        else:
            raise ShopException(f'{self.name.capitalize()} must be not negative integer value!')


class Product:

    """Клас товар. Товар може бути зарезервований - доданий до корзини."""

    amount = NotNegativeValue()

    def __init__(self, item_id, title, price, amount):
        """
        :param item_id: ідентифікатор товару, ціле число
        :param title: назва товару, рядок
        :param price: ціна товару, число
        :param amount: кількість товару, ціле невід'ємне число
        """
        self.item_id = item_id
        self.title = title
        self.price = price
        self.amount = amount

    def __repr__(self):
        """
        :return: повертає рядок-представлення товару
        """
        return f'id: {self.item_id}, {self.title}, price: {self.price}, amount: {self.amount}'

    def take(self, amount):
        """
        Зменшує кількість товару на відповідне значення (додає цей товар до корзини)
        :param amount: кількість товару, ціле число
        """
        self.amount -= amount

    def add(self, amount):
        """
        Збільшує кількість товару на відповідне значення
        (зокрема, забирає цей товар до корзини)
        :param amount: кількість товару, ціле число
        """
        self.amount += amount
