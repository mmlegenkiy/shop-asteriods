from manager import ProductManager, CustomerManager
from my_shop.shop_exceptions import ShopException


class Shop:
    def __init__(self):
        self.products = ProductManager()
        self.customers = CustomerManager()

    def add_to_basket(self, customer_id, product_id, amount):
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        self.products.load()
        product = self.products.find_item(product_id, "Not valid product id")
        if customer is None or product is None:
            raise ShopException
        try:
            product.take(amount)
        except ShopException:
            print(f'Cannot add {amount} items of product with id {product_id} to basket')
        else:
            customer.add_to_basket(product_id, amount)
            self.customers.save()
            self.products.save()

    def take_from_basket(self, customer_id, product_id):
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        self.products.load()
        product = self.products.find_item(product_id, "Not valid product id")
        if customer is None or product is None:
            raise ShopException
        try:
            customer.remove_from_basket(product_id)
        except ShopException:
            print(f"Product with id {product_id} is not in basket of customer with id {customer_id}")
        else:
            product.add(1)
            self.customers.save()
            self.products.save()

    def clear_basket(self, customer_id):
        self.customers.load()
        customer = self.customers.find_item(customer_id, "Not valid customer id")
        if customer is None:
            raise ShopException
        self.products.load()
        for product_id, amount in customer.basket.items():
            product = self.products.find_item(product_id, "Not valid product id")
            if product is None:
                raise ShopException
            product.add(amount)
        customer.clear_basket()
        self.customers.save()
        self.products.save()
