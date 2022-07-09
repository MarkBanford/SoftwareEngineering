from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    """The Chair Interface"""

    @staticmethod
    @abstractmethod
    def get_dimensions():
        "A static interface method"
