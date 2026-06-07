from . import Corsair, Msi
__all__ = ['Corsair','Msi']



class ProtocolError:
    def __init__(self, device: HidDevice, message: str): ...
