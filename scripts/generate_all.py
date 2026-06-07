from generate_namespace_init import processAllNamespaces
from generate_stubs import (
    buildLibreHardwareMonitor,
    buildPyStubbler,
    collectAssembly,
    generateStubs,
    removeExistingStubs,
)
from generate_types_util import generateTypesUtilStub

buildPyStubbler()
buildLibreHardwareMonitor()
collectAssembly()
removeExistingStubs()
generateStubs()
generateTypesUtilStub()
processAllNamespaces()
