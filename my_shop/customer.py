from shop_exceptions import ShopException


class Customer:
    def __init__(self, item_id, name, email, basket):
        """
        :param item_id: ідентифікатор користувача, ціле число
        :param name: ім'я користувача, рядок
        :param email: електронна пошта користувача, рядок
        :param basket: корзина користувача, словник, в якому ключі - ідентифікатори обраних товарів,
        значення кількість цих товарів, обрана користувачем
        """
        self.item_id = item_id
        self.name = name
        self.email = email
        self.basket = basket

    def add_to_basket(self, item_id, amount):
        """
        Додавання товару до корзини. Якщо товар вже в корзині,
        то змінюється його кількість, якщо товару немає в корзині, то він додається.
        :param item_id: ідентифікатор товару, що додається
        :param amount: кількість товару, що додається
        """
        if item_id in self.basket:
            self.basket[item_id] += amount
        else:
            self.basket[item_id] = amount

    def remove_from_basket(self, item_id):
        """
        Видалення товару із корзини. Видаляється по одному. Якщо кількість
        відповідного товару стає рівною нулю, то відповідний запис видаляється
        зі словника-корзини. При спробі видалити товар, якого немає в корзині,
        генерується виняток
        :param item_id: ідентифікатор товару, що видаляється
        """
        if item_id in self.basket:
            self.basket[item_id] -= 1
            if self.basket[item_id] == 0:
                del self.basket[item_id]
        else:
            raise ShopException(f"Product {item_id} is not in the basket")

    def clear_basket(self):
        """Очищення корзини, відповідний словник очищується"""
        self.basket.clear()

    def __repr__(self):
        """
        Магічний метод для відображения інформації про об'єкт класу.
        Якщо корзина є пустою, то друкується  Nothing
        :return:
        """
        message = f'id: {self.item_id}, {self.name}, email: {self.email}\nIn basket:\n'
        if self.basket:
            for item_id, amount in self.basket.items():
                message += f'product_id: {item_id}, amount: {amount}\n'
        else:
            message += 'Nothing\n'
        return message
