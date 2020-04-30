# use when you have tree-like structure or massive
import xml
from xml.etree.ElementTree import ElementTree
from xml.dom import minidom


class Element:

    text = None
    tail = None

    def __init__(self, tag, attrib={}, **extra):
        if not isinstance(attrib, dict):
            raise TypeError("attrib must be dict, not %s" % (
                attrib.__class__.__name__,))
        attrib = attrib.copy()
        attrib.update(extra)
        self.tag = tag
        self.attrib = attrib
        self._children = []

    def __repr__(self):
        return "<%s %r at %#x>" % (self.__class__.__name__, self.tag, id(self))

    def __len__(self):
        return len(self._children)

    def __getitem__(self, index):
        return self._children[index]

    def append(self, subelement):
        self._children.append(subelement)

    def getchildren(self):
        return self._children

    def iter(self, tag=None):
        if tag == "*":
            tag = None
        if tag is None or self.tag == tag:
            yield self
        for e in self._children:
            yield from e.iter(tag)

    def items(self):
        return self.attrib.items()


# create XML
root = Element('root')
tree = ElementTree(root)


root.append(Element('child'))

child_1 = Element('child')
child_1.append(Element('child_of_child'))
root.append(child_1)

child_2 = Element('child')
child_2.text = 'some text'
root.append(child_2)


xmlstr = minidom.parseString(xml.etree.ElementTree.tostring(root)).toprettyxml(indent="   ")
with open("composite/new.xml", "w") as f:
    f.write(xmlstr)

