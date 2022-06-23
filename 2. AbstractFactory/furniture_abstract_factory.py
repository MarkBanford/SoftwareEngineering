from abc import ABCMeta, abstractmethod
from chair_factory import ChairFactory
from table_factory import TableFactory


class IFurnitureFactory(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_furniture(furn_type):
        """The static furniture factory interface method"""


class FurnitureFactory(IFurnitureFactory):
    @staticmethod
    def get_furniture(furn_type):
        try:
            if furn_type in ['BigChair', 'MediumChair', 'SmallChair']:
                return ChairFactory.get_chair(furn_type)
            if furn_type in ['BigTable', 'MediumTable', 'SmallTable']:
                return TableFactory.get_table(furn_type)
            raise AssertionError("Cannot find furniture type")
        except AssertionError as _e:
            print(_e)
        return None


if __name__ == '__main__':
    FURNITURE = FurnitureFactory.get_furniture("BigChair")
    print(FURNITURE.get_dimensions())
