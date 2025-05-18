class Coffee:
    def __init__(self, name):
        self._name = name
        if not isinstance(name, str):
            raise TypeError ('Name must be a string')
        if len(name) < 3:
            raise ValueError ('Name must be at least three characters')


    @property
    def name(self):
        return self._name

# coffee = Coffee("Latte")
# print(Coffee)