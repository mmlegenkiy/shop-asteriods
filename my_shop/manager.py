from file_manager import  FileManager
from product import Product
from customer import Customer
from shop_exceptions import  ShopException
import os.path
import abc


class Manager(abc.ABC):
    def __init__(self):
        self.filename = ''
        self.items = []

    def save(self):
        manager = FileManager()
        try:
            manager.save_to_file(self.filename, self.items)
        except FileNotFoundError:
            print(f'File {self.filename} does not exist')

    @abc.abstractmethod
    def load(self):
        pass

    def get_items(self):
        self.load()
        if self.items:
            for item in self.items:
                print(repr(item))
        else:
            print('No items yet')

    def find_item(self, item_id, message=''):
        self.load()
        for item in self.items:
            if item.item_id == item_id:
                return item
        else:
            if message:
                print(message)
            return None


class ProductManager(Manager):
    def __init__(self):
        super().__init__()
        self.filename = 'data/products.json'

    def load(self):
        manager = FileManager()
        if os.path.exists(self.filename):
            self.items.clear()
            data = manager.load_from_file(self.filename)
            for item in data:
                self.items.append(
                    Product(item_id=item['item_id'], title=item['title'],
                            price=float(item['price']),
                            amount=int(item['amount'])))

    def add_product(self, product_state):
        self.load()
        product = self.find_item(product_state['item_id'])
        if product is not None:
            self.items.remove(product)
        try:
            self.items.append(Product(item_id=product_state['item_id'], title=product_state['title'],
                                         price=float(product_state['price']),
                                         amount=int(product_state['amount'])))
        except KeyError:
            print('Not valid product state')
        self.save()

    def remove_product(self, item_id):
        self.load()
        product = self.find_item(item_id)
        if product is None:
            raise ShopException("Not valid id")
        else:
            self.items.remove(product)
        self.save()


class CustomerManager(Manager):
    def __init__(self):
        super().__init__()
        self.filename = 'data/customers.json'

    def load(self):
        manager = FileManager()
        if os.path.exists(self.filename):
            self.items.clear()
            data = manager.load_from_file(self.filename)
            for item in data:
                self.items.append(
                    Customer(item_id=item['item_id'], name=item['name'],
                            email=item['email'],
                            basket={int(key):int(value) for key, value in item['basket'].items()}))

    def add_customer(self, customer_data):
        self.load()
        customer = self.find_item(customer_data['item_id'])
        if customer is not None:
            self.items.remove(customer)
        try:
            self.items.append(Customer(item_id=customer_data['item_id'], name=customer_data['name'],
                                      email=customer_data['email'], basket={}))
        except KeyError:
            print('Not valid product state')
        self.save()
