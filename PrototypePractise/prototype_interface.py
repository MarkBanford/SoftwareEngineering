from abc import ABCMeta, abstractmethod


class IPrototype(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def clone(mode):
        "Clones the object"
