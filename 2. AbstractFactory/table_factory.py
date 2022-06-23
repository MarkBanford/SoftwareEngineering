from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        """The Table Interface"""


class BigTable(ITable):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"Height": self.height, "Width": self.width, "Depth": self.depth}


class MediumTable(ITable):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"Height": self.height, "Width": self.width, "Depth": self.depth}


class TableFactory:
    @staticmethod
    def get_table(tabletype):
        try:
            if tabletype == "BigTable":
                return BigTable()
            if tabletype == "MediumTable":
                return MediumTable()
            raise AssertionError("Table not found")
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    Table = TableFactory.get_table("BigTable")
    print(Table.get_dimensions())
    print(f"{Table.__class__}")
    Table1 = TableFactory.get_table("MediumTable")
    print(Table1.get_dimensions())
