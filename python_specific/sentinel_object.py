# use for flexibility of your program
# such as None, 0, 1, -1, etc.


def min(iterable, default=None):
    """Imperfect re-implementation of Python's built-in min function."""
    minimum = None
    for item in iterable:
        if minimum is None or item < minimum:
            minimum = item
    if minimum is not None:
        return minimum
    elif default is not None:
        return default
    else:
        raise ValueError("Empty iterable")


# 1st BUG - an iterable containing a single None value will be treated as if it was an empty iterable.
# print(min([None]))  # raising ValueError("Empty iterable"). Expected: None.


def min(iterable, default=None):
    """Imperfect re-implementation of Python's built-in min function."""
    initial = object()
    minimum = initial
    for item in iterable:
        if minimum is initial or item < minimum:
            minimum = item
    if minimum is not initial:
        return minimum
    elif default is not None:
        return default
    else:
        raise ValueError("Empty iterable")


# 2nd BUG - if we specify our default value as None this min function wont accept it.
# print(min([], default=None))  # raising ValueError("Empty iterable"). Expected: None.

# RIGHT IMPLEMENTATION

INITIAL = object()


def min(iterable, default=INITIAL):
    """Imperfect re-implementation of Python's built-in min function."""
    minimum = INITIAL
    for item in iterable:
        if minimum is INITIAL or item < minimum:
            minimum = item
    if minimum is not INITIAL:
        return minimum
    elif default is not INITIAL:
        return default
    else:
        raise ValueError("Empty iterable")


print(min([None]))
print(min([], default=None))
