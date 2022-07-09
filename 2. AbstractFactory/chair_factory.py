from big_chair import BigChair
from small_chair import SmallChair


class ChairFactory:

    @staticmethod
    def get_chair(chair):
        if chair == "SmallChair":
            return SmallChair()
        if chair == "BigChair":
            return BigChair()
        return None
