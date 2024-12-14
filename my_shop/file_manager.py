import json

class FileManager:
    """
    Клас для роботи із файлом-json. До файлу можна зберігати дані про товари або користувачів
    (при цьому зберігається інформація про товари в корзині користувача). Дані після завантаження
    потребують розбору для створення відповідних об'єктів
    """
    @staticmethod
    def save_to_file(file_name, data):
        """
        Для збереження інформації про об'єкти створюється список словників,
        які містить атрибути кожного об'єкта (ключі) та їх зачення.
        :param file_name: назва файлу (або шлях до файлу), де зберігається інформація
        :param data: дані, що зберігаються; мають вигляд списку об'єктів, що зберігаються
        :return:
        """
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
        """
        Метод для завантаження даних із файлу. Дані завантажуються у вигляді
        списку словників, де ключами виступають атрибути об'єкту, а значеннями -
        значення цих атрибутів
        :param file_name: назва файлу (або шлях до файлу), де зберігається інформація
        """
        with open(file_name, "r") as file:
            data = json.load(file)
        return data
