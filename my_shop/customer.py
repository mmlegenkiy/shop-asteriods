from shop_exceptions import ShopException

"""Клас користувач. Має властивості ім'я та електронна пошта. Також має властивість корзина,
 до якої може додавати, видаляти товари із магазину. Корзина є словником, де об'єкту типу 
 товар ставиться у відповідність кількість цього товару, яку додано до корзини. 	"""

class Customer:
    def __init__(self, item_id, name, email, basket):
        self.item_id = item_id
        self.name = name
        self.email = email
        self.basket = basket

    def add_to_basket(self, item_id, amount):
        """Додавання товару до корзини. Якщо товар вже в корзині, то змінюється його кількість,
         якщо товару немає в корзині (у відповідному словнику), то він додається."""
        if item_id in self.basket:
            self.basket[item_id] += amount
        else:
            self.basket[item_id] = amount

    def remove_from_basket(self, item_id):
        """Видалення товару із корзини. Видаляється по одному. Якщо кількість відповідного товару
        стає рівною нулю, то відповідний запис видаляється зі словника-корзини."""
        if item_id in self.basket:
            self.basket[item_id] -= 1
            if self.basket[item_id] == 0:
                del self.basket[item_id]
        else:
            raise ShopException(f"Product {item_id} is not in the basket")

    def clear_basket(self):
        """Очищення корзини"""
        self.basket.clear()

    def __repr__(self):
        message = f'id: {self.item_id}, {self.name}, email: {self.email}\nIn basket:\n'
        if self.basket:
            for item_id, amount in self.basket.items():
                message += f'product_id: {item_id}, amount: {amount}\n'
        else:
            message += 'Nothing\n'
        return message
