# use it to separate the logic and representation
# use when your products
from abc import ABC, abstractmethod


class CoffeeMachine(ABC):

    @property
    @abstractmethod
    def coffee(self):
        pass

    @abstractmethod
    def add_beans(self):
        pass

    @abstractmethod
    def add_water(self):
        pass

    @abstractmethod
    def add_sugar(self):
        pass

    @abstractmethod
    def add_milk(self):
        pass


class CoffeeMachineVitek(CoffeeMachine):

    def __init__(self):
        # should have an empty object to further creation
        self.reset()

    def reset(self):
        self._coffee = Coffee()

    @property
    def coffee(self):
        coffee = self._coffee
        self.reset()
        return coffee

    def add_beans(self):
        self._coffee.add("Beans")

    def add_water(self):
        self._coffee.add("Water")

    def add_sugar(self):
        self._coffee.add("Sugar")

    def add_milk(self):
        self._coffee.add("Milk")


class Coffee:

    def __init__(self):
        self.parts = []

    def add(self, part):
        self.parts.append(part)

    def print_list_parts(self):
        print(f"This drink contains: {', '.join(self.parts)}", end="")


class Barista:
    """
    Honestly, unnecessary class.
    It is used only for defining the order of mixing ingredients.
    """

    def __init__(self):
        self._coffee_builder = None

    @property
    def coffee_builder(self):
        return self._coffee_builder

    @coffee_builder.setter
    def coffee_builder(self, coffee_builder):
        self._coffee_builder = coffee_builder

    def create_espresso(self):
        self.coffee_builder.add_beans()
        self.coffee_builder.add_water()
        print("BARISTA: -Hey! Here is your espresso!")

    def create_latte(self):
        self.coffee_builder.add_beans()
        self.coffee_builder.add_water()
        self.coffee_builder.add_sugar()
        self.coffee_builder.add_sugar()
        self.coffee_builder.add_milk()
        print("BARISTA: -Hey! Here is your latte!")


barista = Barista()
coffee_machine = CoffeeMachineVitek()
barista.coffee_builder = coffee_machine

print("COFFEEMAN: -Create me an espresso!")
barista.create_espresso()
coffee_machine.coffee.print_list_parts()

print("\n")

print("COFFEEMAN: -I want a cup of latte!")
barista.create_latte()
coffee_machine.coffee.print_list_parts()

print("\n")

# Remember: you can just buy a coffee machine to create coffee on your own
print("COFFEEMAN: -I want a sweet water!")
coffee_machine.add_water()
coffee_machine.add_sugar()
coffee_machine.coffee.print_list_parts()
