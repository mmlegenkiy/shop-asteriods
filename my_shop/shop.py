from manager import ProductManager, CustomerManager
from shop_exceptions import ShopException


class Shop:
    """
    Керує взаємодією товарів та користувачів
    """
    def __init__(self):
        """
        Атрибути цього класу менеджер товарів та менеджер користувачів
        """
        self.products = ProductManager()
        self.customers = CustomerManager()

    def add_to_basket(self, customer_id, product_id, amount):
        """
        Додоє до корзини користувача з ідентифікатором customer_id
        amount товарів з ідентифікатором product_id
        :param customer_id: ідентифікатор користувача, ціле число
        :param product_id: ідентифікатор товару, ціле число
        :param amount: кількість одиниць товару, ціле число
        """
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        self.products.load()
        product = self.products.find_item(product_id, "Not valid product id")
        if customer is None or product is None:
            # якщо немає товару із вказаним ідентифікатором
            # або користувача із вказаним ідентифікаторм генеруємо виключення
            raise ShopException
        try:
            # зменшуємо кількість товару на вказане значення
            # та ловимо виключення, якщо це не вдається зробити
            product.take(amount)
        except ShopException:
            print(f'Cannot add {amount} items of product with id {product_id} to basket')
        else:
            customer.add_to_basket(product_id, amount)
            self.customers.save()
            self.products.save()

    def take_from_basket(self, customer_id, product_id):
        """
        Прибираємо з корзини користувача з ідентифікатором customer_id
        один товар з ідентифікатором product_id
        :param customer_id: ідентифікатор користувача, ціле число
        :param product_id: ідентифікатор товару, ціле число
        """
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        self.products.load()
        product = self.products.find_item(product_id, "Not valid product id")
        if customer is None or product is None:
            # якщо немає товару із вказаним ідентифікатором
            # або користувача із вказаним ідентифікаторм генеруємо виключення
            raise ShopException
        try:
            # намагаємось прибрати товар з корзини
            # та ловимо виключення, якщо це не вдається зробити
            customer.remove_from_basket(product_id)
        except ShopException:
            print(f"Product with id {product_id} is not in basket of customer with id {customer_id}")
        else:
            product.add(1)
            self.customers.save()
            self.products.save()

    def clear_basket(self, customer_id):
        """
        Очищуємо корзину користувача з ідентифікатором customer_id
        :param customer_id: ідентифікатор користувача, ціле число
        """
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        if customer is None:
            # якщо немає користувача із вказаним ідентифікатором генеруємо виключення
            raise ShopException
        self.products.load()
        for product_id, amount in customer.basket.items():
            # намагаємось повернути всі товари із корзини користувача
            # якщо зустрічаємось із неправильною інформацією генеруємо виключення
            product = self.products.find_item(product_id, "Not valid product id")
            if product is None:
                raise ShopException
            product.add(amount)
        customer.clear_basket()
        self.customers.save()
        self.products.save()
