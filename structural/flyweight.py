# use when you create lots of instances to save the memory
from sys import intern

# INTS
a = -5
b = -5
print(a is b)  # True

c = 256
d = 256
print(c is d)  # True

e = 's'*21
f = 's'*21
print(e is f)  # False


# intern()
"""
    This enters the string in the (global)
    table of interned strings whose purpose is to speed up dictionary lookups.
    Return the string itself or the previously interned string object with the
    same value.
"""

g = intern('s'*21)
h = 's'*21
print(g is h)  # False

h = intern('s'*21)
print(g is h)  # True


# bool()
k = bool(1)
m = bool(True)
print(k is m)  # True

# OOP
class Grade(object):
    _instances = {}

    def __new__(cls, percent):
        percent = max(50, min(99, percent))
        letter = 'FDCBA'[(percent - 50) // 10]
        self = cls._instances.get(letter)
        if self is None:
            self = cls._instances[letter] = object.__new__(Grade)
            self.letter = letter
        return self

    def __repr__(self):
        return f'Grade {self.letter}'


print(Grade(55), Grade(85), Grade(95), Grade(100))
print(Grade._instances)
print(Grade(95) is Grade(100))  # ask for 'A' two more times
