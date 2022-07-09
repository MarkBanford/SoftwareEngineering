from plane import Plane
from ship import Ship
from truck import Truck


# planDelivery()
# create Transport()

class Logistics:

    @staticmethod
    def delivery_method(method):
        if method == 'Sea':
            return Ship()
        if method == 'Land':
            return Truck()
        if method == "Air":
            return Plane()
        return None


