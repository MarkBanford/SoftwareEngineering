from abc import ABCMeta, abstractmethod


class ITransport(metaclass=ABCMeta):
    """The Transport Interface"""

    @staticmethod
    @abstractmethod
    def deliver():
        "A static interface method"