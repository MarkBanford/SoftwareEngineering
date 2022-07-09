from ITransport import ITransport


class Ship(ITransport):
    def __init__(self):
        pass

    def deliver(self):
        return f'Deleivered by Ship'
