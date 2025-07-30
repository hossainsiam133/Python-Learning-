class Computer:
    def __init__(self):
        self._maxPrice = 900

    def sell(self):
        print(f"Max Price is: {self._maxPrice}")
    def set(self,price):
        self._maxPrice = price

c1 = Computer()
c1.sell()

c1.maxPrice = 1200
c1.sell()

c1.set(1000)
c1.sell()