# use when you want to replace copy-pasting while creation
# when you want to create new instance based on existed

from datetime import datetime
from copy import deepcopy


class Prototype:

    def __init__(self):
        self._primitive = None
        self._component = None
        self._circular_reference = None

    @property
    def primitive(self):
        return self._primitive

    @primitive.setter
    def primitive(self, value):
        self._primitive = value

    @property
    def component(self):
        return self._component

    @component.setter
    def component(self, value):
        self._component = value

    @property
    def circular_reference(self):
        return self._circular_reference

    @circular_reference.setter
    def circular_reference(self, value):
        self._circular_reference = value

    def clone(self):
        self.component = deepcopy(self.component)
        self.circular_reference = deepcopy(self.circular_reference)
        # self.circular_reference.prototype = self
        return deepcopy(self)

    def __str__(self):
        return f"Prototype {id(self)} with primitive id: {id(self.primitive)} component id: {id(self.component)}," \
               f" circular_reference id: {id(self.circular_reference)}"


class ComponentWithBackReference:
    def __init__(self, prototype):
        self._prototype = prototype

    @property
    def prototype(self):
        return self._prototype

    @prototype.setter
    def prototype(self, value):
        self._prototype = value


p1 = Prototype()
p1.primitive = 123
p1.component = datetime.now()
p1.circular_reference = ComponentWithBackReference(p1)

p2 = p1.clone()

print(p1)
print(p2)
