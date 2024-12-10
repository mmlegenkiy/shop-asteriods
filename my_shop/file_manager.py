import json
from product import Product

class FileManager:
    """
    Клас для роботи із файлом-json. До файлу можна зберігати дані (товари) та завантажувати їх звідти.
    """
    @staticmethod
    def save_to_file(file_name, data):
        with open(file_name, "w") as file:
            json.dump([{'title': product.title,'price': product.price,
                        'amount': product.amount} for  product in data], file)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return [Product(title=item['title'], price=float(item['price']), amount=int(item['amount'])) for item in data]
