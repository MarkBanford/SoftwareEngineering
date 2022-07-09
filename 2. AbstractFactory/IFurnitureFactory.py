from abc import ABCMeta, abstractmethod


class IFurniture(metaclass=ABCMeta):
    """The Furniture Interface"""

    @staticmethod
    @abstractmethod
    def get_furniture(f_type):
        "A static interface method"
