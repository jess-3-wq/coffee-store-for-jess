class Order:
    _all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError('Customer must be a Customer instance.')
        if not isinstance(coffee, Coffee):
            raise TypeError('Coffee must be a Coffee instance.')
        if not isinstance(price, (int, float)):
            raise TypeError('Price must be a number.')
        if not (1.0 <= price <= 10.0):
            raise ValueError('Price must be between 1.0 and 10.0.')

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order._all_orders.append(self)

    def __repr__(self):
        return f'Order({self.customer.name}, {self.coffee.name}, ${self.price})'

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all(cls):
        return cls._all_orders
