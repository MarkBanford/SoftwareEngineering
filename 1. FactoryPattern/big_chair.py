from interface_chair import IChair


class BigChair(IChair):

    def __init__(self):
        self._height = 180
        self._width = 180
        self._depth = 180

    def get_dimensions(self):
        return {

            "width": self._width,
            "depth": self._depth,
            "height": self._height

        }
