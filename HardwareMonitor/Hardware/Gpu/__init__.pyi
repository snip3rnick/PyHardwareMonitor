from HardwareMonitor.Hardware import Hardware


class GenericGpu(Hardware):
    def Close(self) -> None: ...
    @property
    def DeviceId(self) -> str: ...
