from abc import ABCMeta, abstractmethod


class IValue(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def __str__():
        "Overides the object to return the value attribute"
