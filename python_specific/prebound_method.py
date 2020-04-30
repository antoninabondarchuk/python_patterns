# use classes and instantiate it to manage the state of it and allow parallelism
from datetime import datetime


class Time(object):
    def __init__(self):
        self.updated_time = datetime.now()

    def update_time(self):
        self.updated_time = datetime.now()
        return self.updated_time


_instance = Time()
_instance_1 = Time()

updated_time = _instance.update_time
updated_time_1 = _instance_1.update_time

print(updated_time)
print(updated_time_1)

print(updated_time())
print(updated_time_1())
