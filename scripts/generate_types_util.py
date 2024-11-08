
import clr  # noqa: F401
from pathlib import Path


BASE_PATH   = Path(__file__).parent.absolute()
MODULE_PATH = BASE_PATH / ".." / "HardwareMonitor"
TYPES_STUB  = MODULE_PATH / "_util" / "types.pyi"

NAMESPACES  = (
    "System", "System.Collections.Generic",
)

EXCLUDE_SYMBOLS = set(["Tuple", "Set", "Iterable", "List"])


# ------------------------------------------------------------------------------
def getExported(namespace):
    split = namespace.split(".", 1)
    fromlist = ()
    if len(split) == 2:
        fromlist = (split[0],)
    module = __import__(namespace, fromlist=fromlist)
    return set([attr for attr in module.__all__ if "`" not in attr]) - EXCLUDE_SYMBOLS


# ------------------------------------------------------------------------------
def generateTypesUtilStub():
    lines = ["# Generated stub file for some types from the CLR\n", "\n"]
    for namespace in NAMESPACES:
        lines.append(f"# Symbols from '{namespace}' namespace\n")
        for symbol in sorted(getExported(namespace), key=str.lower):
            lines.append(f"class {symbol}: ...\n")
        lines.append("\n")
    with open(TYPES_STUB, "w") as fobj:
        fobj.writelines(lines)
    print("generated typing utility")


if __name__ == "__main__":
    generateTypesUtilStub()
