import re
from pathlib import Path

from generate_types_util import NAMESPACES, getExported

SYSTEM_SYMBOLS = set(sum(map(list, map(getExported, NAMESPACES)), start=[]))


BASE_PATH      = Path(__file__).parent.absolute()
MODULE_PATH    = BASE_PATH / ".." / "HardwareMonitor"
NAMESPACE_INIT = BASE_PATH / "namespace.py"
IMPORT_BASE    = "LibreHardwareMonitor"

EXCLUDE_SYMBOLS= ("Type", "Version")


# ------------------------------------------------------------------------------
def findClosingParenthesis(data, symbols="()"):
    sym_open, sym_close = symbols
    lindex = rindex = lcount = rcount = 0
    while rindex > -1:
        rindex = data.find(sym_close, rindex) + 1
        lcount += data.count(sym_open, lindex, rindex)
        if lcount == rcount:
            break
        rcount += 1
        lindex = rindex
    return rindex - 1


# ------------------------------------------------------------------------------
def _replaceSetBracesRecursive(data, pattern: re.Pattern):
    blocks = []
    pos = 0
    while 42:
        match = pattern.search(data, pos)
        if not match:
            break
        _, mend = match.regs[0]
        blocks.append(data[pos:mend-1])
        blocks.append("[")
        remainder = data[mend:]
        rpos = findClosingParenthesis(remainder)
        blocks.extend(_replaceSetBracesRecursive(remainder[:rpos], pattern))
        blocks.append("]")
        pos = mend + rpos + 1
    if pos < (len(data) - 1):
        blocks.append(data[pos:])
    return blocks


# ------------------------------------------------------------------------------
def repairSetAnnotation(stub_data):
    regex   = re.compile(r"(\A|\W)Set\(")
    return ''.join(_replaceSetBracesRecursive(stub_data, regex))


# ------------------------------------------------------------------------------
def repairArrayAnnotation(stub_data):
    return re.sub(r"(\s)([^\s\[]+)\[\,\]", r"\1List[\2]", stub_data)


# ------------------------------------------------------------------------------
def repairTypingImport(stub_data):
    return stub_data.replace("from typing import ", "from typing import overload, ")


# ------------------------------------------------------------------------------
def addSystemSymbolImport(stub_data):
    symbol_patterns = [(s, f"\\W{s}\\W") for s in SYSTEM_SYMBOLS]
    symbols_used = set()
    for symbol, pattern in symbol_patterns:
        if re.search(pattern, stub_data):
            symbols_used.add(symbol)
    symbols_used = symbols_used.difference(EXCLUDE_SYMBOLS)
    if not symbols_used:
        return stub_data
    insert_index = stub_data.find("from typing import")
    symbols_str = ", ".join(sorted(symbols_used))
    import_statement = f"from HardwareMonitor._util.types import {symbols_str}\n"
    return stub_data[:insert_index] + import_statement + stub_data[insert_index:]


# ------------------------------------------------------------------------------
def repairStub(stub_path: Path):
    repair_steps = [
        repairSetAnnotation,
        repairArrayAnnotation,
        repairTypingImport,
        addSystemSymbolImport,
    ]
    with stub_path.open("r") as fobj:
        stub_data = fobj.read()
    # Apply repair functions to the data
    for func in repair_steps:
        stub_data = func(stub_data)
    with stub_path.open("w") as fobj:
        fobj.write(stub_data)
    print("repaired", repr(str(stub_path.relative_to(BASE_PATH))))


# ------------------------------------------------------------------------------
def processNamespaceDir(namespace_dir: Path):
    has_subdirs = False
    init_py = namespace_dir / "__init__.py"
    options = {
        "namespace_root":   IMPORT_BASE,
        "submodule_name":   namespace_dir.relative_to(MODULE_PATH).as_posix().replace("/", "."),
    }
    for path in namespace_dir.iterdir():
        if path.is_dir():
            processNamespaceDir(path)
            has_subdirs = True
        if path.name == "__init__.pyi":
            with open(NAMESPACE_INIT, "r") as fin:
                with open(init_py, "w") as fout:
                    fout.write(fin.read().format(**options))
            print("updated ", repr(str(init_py.relative_to(BASE_PATH))))
            repairStub(path)

    if has_subdirs:
        init_py.touch(exist_ok=True)
        print("touched ", repr(str(init_py.relative_to(BASE_PATH))))


# ------------------------------------------------------------------------------
for path in MODULE_PATH.iterdir():
    if path.is_dir():
        processNamespaceDir(path)
