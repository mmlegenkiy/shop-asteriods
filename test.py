import json

lst = [{'title': 'Mobile Phone', 'price': 60, 'amount': 10}, {'title': 'Notebook', 'price': 300, 'amount': 5}, {'title': 'Power Bank', 'price': 20, 'amount': 15}, {'title': 'Headphone', 'price': 15, 'amount': 20}]
with open('test.json', "w") as file:
    json.dump([{'title': product.title, 'price': product.price,
                'amount': product.amount} for product in data], file_name)