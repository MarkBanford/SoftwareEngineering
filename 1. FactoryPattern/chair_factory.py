from abc import ABCMeta, abstractmethod


class IChair(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def get_dimensions():
        """The Chair Interface"""


class BigChair(IChair):
    def __init__(self):
        self.height = 80
        self.width = 80
        self.depth = 80

    def get_dimensions(self):
        return {"Height": self.height, "Width": self.width, "Depth": self.depth}


class MediumChair(IChair):
    def __init__(self):
        self.height = 70
        self.width = 70
        self.depth = 70

    def get_dimensions(self):
        return {"Height": self.height, "Width": self.width, "Depth": self.depth}


class ChairFactory:
    @staticmethod
    def get_chair(chair_type):
        try:
            if chair_type == "BigChair":
                return BigChair()
            if chair_type == "MediumChair":
                return MediumChair()
            raise AssertionError("Chair not found")
        except AssertionError as _e:
            print(_e)


if __name__ == '__main__':
    CHAIR = ChairFactory.get_chair("BigChair")
    print(CHAIR.get_dimensions())
    print(f"{CHAIR.__class__}")
    CHAIR1 = ChairFactory.get_chair("MediumChair")
    print(CHAIR1.get_dimensions())
