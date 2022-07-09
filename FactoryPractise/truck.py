from ITransport import ITransport


class Truck(ITransport):
    def __init__(self):
        pass

    def deliver(self):
        return f'Deleivered by Truck'