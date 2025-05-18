class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all_orders.append(self)
         
        if not isinstance(customer, Customer):
            raise TypeError('Customer has to be a Customer instance.')
        if not isinstance(coffee, Coffee):
            raise TypeError('Coffee should be a Coffee instance.') 
        if not (1.0 <= price <= 10.0):
            raise ValueError('Price ought to be between 1.0 and 10.0')
        if not isinstance(price, (int, float)):
            raise TypeError('Price should be an integer')


    @property
    def price (self):
        return self._price

    @property
    def coffee (self):
        return self._coffee

    @property
    def customer (self):
        return self._customer
                        
    @classmethod
    def all_orders (cls):
        return cls.all.orders 

from customer import Customer
from coffee import Coffee
from order import Order

customer = Customer("Jesse")
print(customer)
coffee = Coffee("Latte")
print(coffee)  
price = 50
print(price)    


