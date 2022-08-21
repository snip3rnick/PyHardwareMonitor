# Gerneric namespace __init__.py file loading all exported sysmbols from the reference resource

from HardwareMonitor import ASSEMBLY_NAME

__reference_name__    = ".".join([ASSEMBLY_NAME, __name__.split(".", 1)[-1]])
__reference_package__ = __reference_name__.split(".", 1)[0]
__reference_module__  = __import__(__reference_name__, fromlist=(__reference_package__,))

globals().update(dict(map(
    lambda attr: (attr, getattr(__reference_module__, attr)),
    __reference_module__.__all__
)))
