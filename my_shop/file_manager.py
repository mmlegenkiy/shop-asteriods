import json

class FileManager:
    """
    Клас для роботи із файлом-json. До файлу можна зберігати дані (товари) та завантажувати їх звідти.
    """
    @staticmethod
    def save_to_file(file_name, data):
        list_for_writing = []
        if data:
            attributes = data[0].__dict__.keys()
            for item in data:
                item_dict = {}
                for attribute in attributes:
                    item_dict[attribute] = getattr(item, attribute)
                list_for_writing.append(item_dict)
        with open(file_name, "w") as file:
            json.dump(list_for_writing, file)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
