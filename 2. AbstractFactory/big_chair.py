from IChair import IChair


class BigChair(IChair):
    def __init__(self):
        self.height = 160
        self.width = 160
        self.depth = 160

    def get_dimensions(self):
        return {
            "height": self.height,
            "width": self.width,
            "depth": self.depth

        }
