from shop_exceptions import ShopException
from order import Order


class Shop:
    def __init__(self):
        """Клас магазин. Містить список користувачів, товарів та замовлень."""
        self.customers = []
        self.products = []
        self.orders = []

    def add_customer(self, customer):
        """Додати користувача"""
        self.customers.append(customer)

    def add_product(self, product):
        """Додати товар"""
        self.products.append(product)

    def reserve_product(self, product, amount, customer):
        """Додати відповдіну кількість товару до корзини користувача"""
        if product in self.products and customer in self.customers:
            product.reserve(amount)
            customer.add_to_basket(product, amount)
        else:
            raise ShopException("Wrong product or customer")

    def place_order(self, customer, delivery_address):
        """Сформувати замовлення для користувача. Перебирає всі товари,
         які додано до корзини користувача, прибирає їх із резерву,
         очищує корзину та формує екзепляр класу замовлення,
         який додається до переліку замовлень магазину. """
        products = []
        amounts = []
        to_pay = 0
        for product, amount in customer.basket.items():
            products.append(product)
            amounts.append(amount)
            to_pay += product.price * amount
            product.take_from_reserve(amount)
        customer.clear_basket()
        my_order = Order(customer, products, amounts, to_pay, delivery_address)
        self.orders.append(my_order)
