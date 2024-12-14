from file_manager import FileManager
import os

class CustomerManager:
    def __init__(self):
        self.filename = '../my_shop/data/customers.json'
        self.customers = []

    def save(self):
        manager = FileManager()
        try:
            manager.save_to_file(self.filename, self.customers)
        except FileNotFoundError:
            print(f'File {self.filename} does not exist')

    def load(self):
        manager = FileManager()
        if os.path.exists(self.filename):
            self.i.clear()
            data = manager.load_from_file(self.filename)
            for item in data:
                self.products.append(
                    Product(product_id=item['product_id'], title=item['title'],
                            price=float(item['price']),
                            amount=int(item['amount'])))

        # def __init__(self, name, email):
        #     self.name = name
        #     self.email = email
        #     self.basket = {}