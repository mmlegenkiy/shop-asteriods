class Order:

    """Клас замовлення. Збирає всю інформацію щодо замовлення та додає адресу доставки.
    Властивості products та amounts є списками, що містять замовлені товари та, відповідно, їх кількість"""

    def __init__(self, customer, products, amounts, to_pay, delivery_address):
        self.customer = customer
        self.products = products
        self.amounts = amounts
        self.to_pay = to_pay
        self.delivery_address = delivery_address

    def __repr__(self):
        """Друкування інформації про замовлення"""
        message = f"Customer {self.customer.name} with email {self.customer.email} ordered"
        for amount, product in zip(self.amounts, self.products):
            message += f" {amount} of {product.title}, "
        message = message[:len(message) - 2] + f' with delivery address {self.delivery_address}'
        message += f' to pay {self.to_pay} dollars'
        return message
