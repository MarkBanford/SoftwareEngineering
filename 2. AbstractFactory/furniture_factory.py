from IFurnitureFactory import IFurniture
from chair_factory import ChairFactory
from table_factory import TableFactory


class FurnitureFactory(IFurniture):

    @staticmethod
    def get_furniture(f_type):
        try:
            if f_type in ['BigChair', 'SmallChair']:
                return ChairFactory.get_chair(f_type)
            if f_type in ['BigTable', 'SmallTable']:
                return TableFactory.get_table(f_type)
            raise AssertionError("Cannot find furn type")
        except AssertionError as _e:
            print(_e)
        return None
