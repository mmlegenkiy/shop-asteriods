from file_manager import  FileManager
from product import Product
from customer import Customer
from shop_exceptions import ShopException
import os.path
import abc


class Manager(abc.ABC):
    """
    Абстрактний клас, що реалізує загальні властивості менеджера товарів та користувачів
    """
    def __init__(self):
        """
        свтворюються загальні атрибути: назва файлу для зберігання інформації
        (нижче конкретизується для конкретного нащадка) та список сутностей,
        якими керує менеджер
        """
        self.filename = ''
        self.items = []

    def save(self):
        """
        Метод для зберігання інформації до файлу,
        генерує виняток у випадку, якщо не знайде файл
        """
        manager = FileManager()
        try:
            manager.save_to_file(self.filename, self.items)
        except FileNotFoundError:
            print(f'File {self.filename} does not exist')

    @abc.abstractmethod
    def load(self):
        """
        абстрактний метод для завантаження даних із файлу,
        нижче конкретизується для класів нащадків
        :return:
        """
        pass

    def get_items(self):
        """
        клас для друкування інформації про всі сутності
        виводе повідомлення за відсутності сутностей
        """
        self.load()
        if self.items:
            for item in self.items:
                print(item)
        else:
            print('No items yet')

    def find_item(self, item_id, message=''):
        """
        метод для пошуку сутності за її ідентифікатором
        за наяності другого аргумента виводе відповідне повідомлення,
        якщо сутності із вказаним ідентифікатором не існує
        :param item_id: ідентифікатор сутності, ціле число
        :param message: повідомлення, рядок (за замовчуванням: пустий рядок)
        :return: повертає знайдену сутність або None якщо сутність не знайдено
        """
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
        """
        конкретизується файл для зберігання інформації
        """
        super().__init__()
        self.filename = 'data/products.json'

    def load(self):
        """
        реалізовано абстрактний метод із батьківського класа
        """
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
        """метод для додавання товару
        аргументом методу є словник, в якому назвам атрибутів класу товар
        ставляться у відповідність їх значення
        метод може використовуватись також для зміни наявного товараа,
        тому спочатку перевіряється, чи існує товар із вказаним ідентифікатором,
        і якщо такий товар існує, то він модифікується (стара інформація видаляється)"""
        self.load()
        product = self.find_item(product_state['item_id'])
        if product is not None:
            self.items.remove(product)
        try:
            self.items.append(Product(item_id=product_state['item_id'], title=product_state['title'],
                                      price=float(product_state['price']), amount=int(product_state['amount'])))
        except KeyError:
            print('Not valid product state')
        self.save()

    def remove_product(self, item_id):
        """
        метод для видалення товару із вказаним ідентифікатором,
        за відсутності товару з таким ідентифікатором генерується виключення
        :param item_id: ідентифікатор товару, ціле число
        """
        self.load()
        product = self.find_item(item_id)
        if product is None:
            raise ShopException("Not valid id")
        else:
            self.items.remove(product)
        self.save()


class CustomerManager(Manager):
    def __init__(self):
        """
        конкретизується файл для зберігання інформації
        """
        super().__init__()
        self.filename = 'data/customers.json'

    def load(self):
        """
        реалізовано абстрактний метод із батьківського класа
        """
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
        """метод для додавання користувача
        аргументом методу є словник, в якому назвам атрибутів класу користувач
        ставляться у відповідність їх значення
        метод може використовуватись також для зміни наявного користувача,
        тому спочатку перевіряється, чи існує користувач із вказаним ідентифікатором,
        і якщо такий користувач існує, то він модифікується (стара інформація видаляється)
        """
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
