from prototype_interface import IPrototype
import copy


class Document(IPrototype):
    def __init__(self, name, lst):
        self.name = name
        self.list = lst

    def clone(self, mode):

        if mode == 1:
            doc_list = self.list  # shallow copy
        if mode == 2:
            doc_list = self.list.copy()  # level 2 copy
        if mode == 3:
            doc_list = copy.deepcopy(self.list)

        return type(self)(

            self.name,
            doc_list
        )

    def __str__(self):
        return f'Memory address is {id(self)}\tname={self.name}\tlist={self.list}'
