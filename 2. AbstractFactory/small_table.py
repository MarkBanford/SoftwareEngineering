from ITable import ITable


class SmallTable(ITable):
    def __init__(self):
        self.height = 800
        self.width = 800
        self.depth = 800

    def get_dimensions(self):
        return {
            "height": self.height,
            "width": self.width,
            "depth": self.depth

        }
