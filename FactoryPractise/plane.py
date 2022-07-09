from ITransport import ITransport


class Plane(ITransport):
    def __init__(self):
        pass

    def deliver(self):
        return f'Deleivered by Plane'
