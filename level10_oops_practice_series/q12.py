# Q12. Create multilevel inheritance.

class Grandparent:

    def grandparent_method(self):
        print("Grandparent method")


class Parent(Grandparent):

    def parent_method(self):
        print("Parent method")


class Child(Parent):

    def child_method(self):
        print("Child method")


child = Child()

child.grandparent_method()
child.parent_method()
child.child_method()