from interface_prototype import IPrototype


class MyClass(IPrototype):

    def __init__(self, field):
        self.field = field

    def clone(self):
        return type(self)(  # says give me a new instance of my class (default shallow copy)

            self.field.copy()
        )

    def __str__(self):
        return f'Memory address is {id(self)}\tfield={self.field}'
