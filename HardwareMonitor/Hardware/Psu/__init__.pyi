__all__ = ['Corsair','Msi']


class ProtocolError:
    def __init__(self, device: HidDevice, message: str): ...
