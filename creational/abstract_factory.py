# when you want to create some families of products
from abc import ABCMeta, abstractmethod


class Animal:
    def __init__(self, name):
        self.name = name


class Bear(Animal):
    pass


class TeddyBear(Bear):
    pass


class WoodenBear(Bear):
    pass


class Cat(Animal):
    pass


class TeddyCat(Cat):
    pass


class WoodenCat(Cat):
    pass


class AbstractToysFactory(metaclass=ABCMeta):

    @abstractmethod
    def get_bear(self):
        pass

    @abstractmethod
    def get_cat(self):
        pass


class TeddyToysFactory(AbstractToysFactory):
     
    def get_bear(self):
        return TeddyBear("New Teddy Bear")

    def get_cat(self):
        return TeddyCat("New Teddy Cat")


class WoodenToysFactory(AbstractToysFactory):

    def get_bear(self):
        return WoodenBear("New Wooden Bear")

    def get_cat(self):
        return WoodenCat("New Wooden Cat")


# Using factories
toyFactory = WoodenToysFactory()
# toyFactory = TeddyToysFactory()  # uncomment to see the marvel!
bear = toyFactory.get_bear()
cat = toyFactory.get_cat()
print(f"I've got a {bear.name} and a {cat.name}!")


