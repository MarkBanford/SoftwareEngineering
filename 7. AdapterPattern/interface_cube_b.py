from abc import ABCMeta, abstractmethod


class ICubeB(metaclass=ABCMeta):
    @staticmethod
    @abstractmethod
    def create(top_left_front, bottom_right_back):
        "Create a cube by B"
