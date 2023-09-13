#3.5B ARVORE GENEALÓGICA

class Person:
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

    def get_ancestors(self):
        ancestors = []
        current_person = self.parent
        while current_person:
            ancestors.append(current_person.name)
            current_person = current_person.parent
        return ancestors


import unittest

class TestPerson(unittest.TestCase):
    def test_add_child(self):
        parent = Person("Parent")
        child = Person("Child")
        parent.add_child(child)

        self.assertEqual(child.parent, parent)
        self.assertIn(child, parent.children)

    def test_get_ancestors(self):
        grandparent = Person("Grandparent")
        parent = Person("Parent", grandparent)
        child = Person("Child", parent)

        self.assertEqual(child.get_ancestors(), ["Parent", "Grandparent"])
        self.assertEqual(parent.get_ancestors(), ["Grandparent"])
        self.assertEqual(grandparent.get_ancestors(), [])

if __name__ == '__main__':
    unittest.main()

