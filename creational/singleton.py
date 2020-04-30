# use when you want to unify the object. Instance should be shared and exclusive.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Creating new instance...")
            cls._instance = super().__new__(cls)
        return cls._instance


first = Singleton()
second = Singleton()
print(first is second)
