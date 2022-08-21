import re
import shutil
from pathlib import Path

from generate_types_util import NAMESPACES, getExported

SYSTEM_SYMBOLS = set(sum(map(list, map(getExported, NAMESPACES)), start=[]))


BASE_PATH      = Path(__file__).parent.absolute()
MODULE_PATH    = BASE_PATH / ".." / "HardwareMonitor"
NAMESPACE_INIT = BASE_PATH / "namespace.py"


def addSystemSymbolImport(stub_data):
    symbol_patterns = [(s, f"\\W{s}\\W") for s in SYSTEM_SYMBOLS]
    symbols_used = set()
    for symbol, pattern in symbol_patterns:
        if re.search(pattern, stub_data):
            symbols_used.add(symbol)
    if not symbols_used:
        return stub_data
    insert_index = stub_data.find("from typing import")
    symbols_str = ", ".join(sorted(symbols_used))
    import_statement = f"from HardwareMonitor._util.types import {symbols_str}\n"
    return stub_data[:insert_index] + import_statement + stub_data[insert_index:]


def repairStub(stub_path: Path):
    regex_replace = [
        (r"(\s)Set\(([^\)]+)\)", r"\1Set[\2]"),
    ]
    with stub_path.open("r") as fobj:
        stub_data = fobj.read()
    for pattern, repl in regex_replace:
        stub_data = re.sub(pattern, repl, stub_data)
    stub_data = stub_data.replace("from typing import ", "from typing import overload, ")
    stub_data = addSystemSymbolImport(stub_data)
    with stub_path.open("w") as fobj:
        fobj.write(stub_data)
    print("repaired", repr(str(stub_path.relative_to(BASE_PATH))))


def processNamespaceDir(namespace_dir: Path):
    has_subdirs = False
    init_py = namespace_dir / "__init__.py"
    for path in namespace_dir.iterdir():
        if path.is_dir():
            processNamespaceDir(path)
            has_subdirs = True
        if path.name == "__init__.pyi":
            shutil.copyfile(str(NAMESPACE_INIT), str(init_py))
            print("updated ", repr(str(init_py.relative_to(BASE_PATH))))
            repairStub(path)

    if has_subdirs:
        init_py.touch(exist_ok=True)
        print("touched ", repr(str(init_py.relative_to(BASE_PATH))))


for path in MODULE_PATH.iterdir():
    if path.is_dir():
        processNamespaceDir(path)
