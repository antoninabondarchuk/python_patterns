class OddNumbers(object):
    """An iterable object."""

    def __init__(self, maximum):
        self.maximum = maximum

    def __iter__(self):
        print("HELLO FROM THE OUTSIDE!")
        return OddIterator(self)


class OddIterator(object):
    """An iterator."""

    def __init__(self, container):
        self.container = container
        self.n = -1

    def __next__(self):
        self.n += 2
        if self.n > self.container.maximum:
            raise StopIteration
        return self.n

    def __iter__(self):
        return self


odd_iterable = OddNumbers(50)
print(odd_iterable)
print(list(odd_iterable))


odd_iterator = iter(odd_iterable)
print(next(odd_iterator))
print(next(odd_iterator))
