class Coffee:
    def __init__(self, name):
        self._name = name
        if not isinstance(name, str):
            raise TypeError ('Name must be a string')
        if len(name) < 3:
            raise ValueError ('Name must be at least three characters')

    def num_orders(self):
        return sum(1 for order in Order.all_orders if order.coffee == self)

    def average_price(self):
        prices = [order.price for order in Order.all_orders if order.coffee == self]
        if not prices:
        return 0
        return sum(prices) / len(prices)

    @property
    def name(self):
        return self._name

    from order import Order    

# coffee = Coffee("Latte")
# print(Coffee)