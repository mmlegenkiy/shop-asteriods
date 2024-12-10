from shop_exceptions import ShopException

"""Клас користувач. Має властивості ім'я та електронна пошта. Також має властивість корзина,
 до якої може додавати, видаляти товари із магазину. Корзина є словником, де об'єкту типу 
 товар ставиться у відповідність кількість цього товару, яку додано до корзини. 	"""

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.basket = {}

    def add_to_basket(self, product, amount):
        """Додавання товару до корзини. Якщо товар вже в корзині, то змінюється його кількість,
         якщо товару немає в корзині (у відповідному словнику), то він додається."""
        product.reserve(amount)
        if product in self.basket:
            self.basket[product] += amount
        else:
            self.basket[product] = amount

    def remove_from_basket(self, product):
        """Видалення товару із корзини. Видаляється по одному. Якщо кількість відповідного товару
        стає рівною нулю, то відповідний запис видаляється зі словника-корзини."""
        if product in self.basket:
            self.basket[product] -= 1
            if self.basket[product] == 0:
                del self.basket[product]
        else:
            raise ShopException(f"Product {product} is not in the basket")

    def clear_basket(self):
        """Очищення корзини"""
        self.basket.clear()
