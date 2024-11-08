import re
from pathlib import Path

from generate_types_util import NAMESPACES, getExported

SYSTEM_SYMBOLS   = set(sum(map(list, map(getExported, NAMESPACES)), start=[]))
HARDWARE_SYMBOLS = set()


BASE_PATH      = Path(__file__).parent.absolute()
MODULE_PATH    = BASE_PATH / ".." / "HardwareMonitor"
NAMESPACE_INIT = BASE_PATH / "namespace_template.py"
IMPORT_BASE    = "LibreHardwareMonitor"

EXCLUDE_SYMBOLS  = ("Type", "Version", "OperatingSystem")
OVERRIDE_SYMBOLS = ("Single", )
EXTRA_TYPING     = ("overload", )


# ------------------------------------------------------------------------------
def findClosingParenthesis(data: str, symbols="()"):
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
def _replaceSetBracesRecursive(data: str, pattern: re.Pattern):
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
def repairSetAnnotation(stub_data: str):
    regex   = re.compile(r"(\A|\W)Set\(")
    return ''.join(_replaceSetBracesRecursive(stub_data, regex))


# ------------------------------------------------------------------------------
def repairArrayAnnotation(stub_data: str):
    return re.sub(r"(\s)([^\s\[]+)\[\,\]", r"\1List[\2]", stub_data)


# ------------------------------------------------------------------------------
def repairTypingImport(stub_data: str):
    prefix    = "from typing import "
    start_pos = stub_data.find(prefix)
    if start_pos == -1:
        return stub_data
    end_pos   = stub_data.find("\n", start_pos) + 1
    symbols_used  = set()
    stub_data_aft = stub_data[end_pos:]
    all_symbols   = [*EXTRA_TYPING, *map(str.strip, stub_data[start_pos + len(prefix):end_pos].split(","))]
    for symbol in all_symbols:
        if re.search(f"\\W{symbol}\\W", stub_data_aft):
                symbols_used.add(symbol)
    if not symbols_used:
        return stub_data[:start_pos] + stub_data_aft
    import_statement = "from typing import " + ", ".join(sorted(symbols_used)) + "\n"
    return stub_data[:start_pos] + import_statement + stub_data_aft


# ------------------------------------------------------------------------------
def _addSymbolImport(stub_data: str, symbols: set[str], namespace: str):
    symbols_used    = set()
    exists_pos  = stub_data.find(f"from {namespace} import ")
    if exists_pos >= 0:
        keep_index = stub_data.find("\n", exists_pos) + 1
    else:
        keep_index = exists_pos = 0
    stub_data_aft = stub_data[keep_index:]
    for symbol in symbols:
        if re.search(f"\\W{symbol}\\W", stub_data_aft):
            if symbol in OVERRIDE_SYMBOLS or not re.search(f"\\s*(class|def)\\s+{symbol}\\W", stub_data_aft):
                symbols_used.add(symbol)
    symbols_used = symbols_used.difference(EXCLUDE_SYMBOLS)
    if not symbols_used:
        return stub_data
    symbols_str = ", ".join(sorted(symbols_used))
    import_statement = f"from {namespace} import {symbols_str}\n"
    return stub_data[:exists_pos] + import_statement + stub_data_aft


# ------------------------------------------------------------------------------
def addSystemSymbolImport(stub_data: str):
    return _addSymbolImport(stub_data, SYSTEM_SYMBOLS, "HardwareMonitor._util.types")


# ------------------------------------------------------------------------------
def addHardwareSymbolImport(stub_data: str):
    if not HARDWARE_SYMBOLS:
        stub_path = MODULE_PATH / "Hardware" / "__init__.pyi"
        with stub_path.open("r") as fobj:
            for symbol in re.findall("class (\w+)\\W", fobj.read()):
                HARDWARE_SYMBOLS.add(symbol)
    return _addSymbolImport(stub_data, HARDWARE_SYMBOLS, "HardwareMonitor.Hardware")


# ------------------------------------------------------------------------------
def repairStub(stub_path: Path):
    repair_steps = [
        repairSetAnnotation,
        repairArrayAnnotation,
        repairTypingImport,
        addSystemSymbolImport,
        addHardwareSymbolImport,
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
def processAllNamespaces():
    for path in MODULE_PATH.iterdir():
        if path.is_dir():
            processNamespaceDir(path)


if __name__ == "__main__":
    processAllNamespaces()
