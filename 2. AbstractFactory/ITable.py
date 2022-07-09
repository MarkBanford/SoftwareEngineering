from abc import ABCMeta, abstractmethod


class ITable(metaclass=ABCMeta):
    """The Table Interface"""

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"
