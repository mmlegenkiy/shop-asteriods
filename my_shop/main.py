from shop_exceptions import ShopException
from shop import Shop

if __name__ == '__main__':
    my_shop = Shop() # магазин
    my_product_manager = my_shop.products # для зручного керування товарами
    my_customer_manager = my_shop.customers # для зручного керування користувачами

    while True:
        message = ("---------------------------\n"
                   "0. Exit\n1. List of products\n2. Add/modify product\n3. Delete product"
                   "\n4. List of customers\n5. Add customer\n6. Add product to basket"
                   "\n7. Take from basket\n8. Clear basket")
        print(message)
        try:
            user_input = int(input('Enter your choice: '))
        except ValueError:
            print('Input integer number from 0 to 3')
            continue
        match user_input:
            case 0:
                print('Exiting ...')
                break
            case 1:
                my_product_manager.get_items()
            case 2:
                product_state = {}
                try:
                    product_state['item_id'] = int(input('Enter product id: '))
                    product_state['title'] = input('Enter product title: ')
                    product_state['price'] = float(input('Enter product price: '))
                    product_state['amount'] = int(input('Enter product amount: '))
                    my_product_manager.add_product(product_state)
                except ValueError:
                    print('Not valid data')
                except KeyError:
                    print('Not valid data')
                except ShopException:
                    print('Amount should be not negative numbers')
            case 3:
                try:
                    product_id = int(input('Enter product id to delete: '))
                    my_product_manager.remove_product(product_id)
                except ValueError:
                    print('Not valid product id')
                except ShopException:
                    print('Not valid product id')
            case 4:
                my_customer_manager.get_items()
            case 5:
                customer_data = {}
                try:
                    customer_data['item_id'] = int(input('Enter customer id: '))
                    customer_data['name'] = input('Enter customer name: ')
                    customer_data['email'] = input('Enter customer email: ')
                    my_customer_manager.add_customer(customer_data)
                except ValueError:
                    print('Not valid data')
                except KeyError:
                    print('Not valid data')
            case 6:
                customer_id = int(input('Enter customer id: '))
                product_id = int(input('Enter product id: '))
                amount = int(input('Enter amount: '))
                try:
                    my_shop.add_to_basket(customer_id, product_id, amount)
                except ShopException:
                    print(
                        f'Cannot add {amount} of product with id {product_id} to basket of customer with id {customer_id}')
            case 7:
                customer_id = int(input('Enter customer id: '))
                product_id = int(input('Enter product id: '))
                try:
                    my_shop.take_from_basket(customer_id, product_id)
                except ShopException:
                    print(
                        f'Cannot take product with id {product_id} from basket of customer with id {customer_id}')
            case 8:
                customer_id = int(input('Enter customer id: '))
                try:
                    my_shop.clear_basket(customer_id)
                except ShopException:
                    print(
                        f'Cannot clear the basket of customer with id {customer_id}')
            case _:
                print('Not valid choice')
