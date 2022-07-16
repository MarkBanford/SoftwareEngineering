from abc import ABCMeta, abstractmethod


class IShapeImplementer(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def draw_implementation():
        "The method that the refined abstractions will implement"
