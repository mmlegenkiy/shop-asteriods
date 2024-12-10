from shop import Shop
from customer import Customer
from product import Product
from file_manager import FileManager

if __name__ == "__main__":
    # екземпляр магазину
    my_shop = Shop()

    # створюємо користувачів та додаємо їх до магазину
    customer_1 = Customer('Ivan', 'ivan123@gmail.com')
    customer_2 = Customer('Petro', "petro_shevchuk@gmail.com")
    my_shop.add_customer(customer_1)
    my_shop.add_customer(customer_2)

    # створюємо товари
    # product_1 = Product('Mobile Phone', 60, 10)
    # product_2 = Product('Notebook', 300, 5)
    # product_3 = Product('Power Bank', 20, 15)
    # product_4 = Product('Headphone', 15, 20)
    # my_shop.add_product(product_1)
    # my_shop.add_product(product_2)
    # my_shop.add_product(product_3)
    # my_shop.add_product(product_4)

    # товари записано до файлу та їх список завантажується звідти
    file_name = 'products.json'
    # FileManager.save_to_file(file_name, my_shop.products)
    loaded_products = FileManager.load_from_file(file_name)
    for product in loaded_products:
        my_shop.add_product(product)

    # додаємо товари до корзин користувачів
    my_shop.reserve_product(loaded_products[0], 2, customer_1)
    my_shop.reserve_product(loaded_products[1], 1, customer_1)
    my_shop.reserve_product(loaded_products[2], 3, customer_1)
    my_shop.reserve_product(loaded_products[3], 2, customer_1)
    my_shop.reserve_product(loaded_products[0], 3, customer_2)
    my_shop.reserve_product(loaded_products[2], 4, customer_2)

    # формуємо замовлення та друкуємо інформацію про них
    my_shop.place_order(customer_1, 'address 1')
    my_shop.place_order(customer_2, 'address 2')
    for order in my_shop.orders:
        print(repr(order))
