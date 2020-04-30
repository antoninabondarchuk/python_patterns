# use when you want to expand the functionality of some class
# you have one base and many options above it
# IT IS NOT ABOUT PYTHON DECORATORS (see adapter)
from abc import abstractmethod


class BasicCoffee:

    @abstractmethod
    def get_coffee(self):
        return "Basic coffee"


class Latte(BasicCoffee):
    def get_coffee(self):
        return "Latte"


class BasicCoffeeDecorator(BasicCoffee):
    _basic_coffee = None

    def __init__(self, basic_coffee):
        super().__init__()
        self._basic_coffee = basic_coffee

    @property
    def basic_coffee(self):
        return self._basic_coffee

    def get_coffee(self):
        self._basic_coffee.get_coffee()


class Milk(BasicCoffeeDecorator):
    def get_coffee(self):
        return f"{self.basic_coffee.get_coffee()} with Milk"


class Sugar(BasicCoffeeDecorator):
    def get_coffee(self):
        return f"{self.basic_coffee.get_coffee()} with Sugar"


my_basic_coffee = BasicCoffee()
print(f"Working with {my_basic_coffee.get_coffee()}")


my_basic_coffee_with_milk = Milk(my_basic_coffee)
print(f"Working with {my_basic_coffee_with_milk.get_coffee()}")


my_basic_coffee_with_milk_sugar = Sugar(my_basic_coffee_with_milk)
print(f"Working with {my_basic_coffee_with_milk_sugar.get_coffee()}")
