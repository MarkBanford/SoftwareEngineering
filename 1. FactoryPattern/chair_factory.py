from interface_chair import IChair
from small_chair import SmallChair
from big_chair import BigChair


class ChairFactory:

    @staticmethod
    def get_chair(chair):
        if chair == 'BigChair':
            return BigChair()
        if chair == 'SmallChair':
            return SmallChair()
        return None
