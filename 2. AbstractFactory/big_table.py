from ITable import ITable


class BigTable(ITable):
    def __init__(self):
        self.height = 1600
        self.width = 1600
        self.depth = 1600

    def get_dimensions(self):
        return {
            "height": self.height,
            "width": self.width,
            "depth": self.depth

        }
