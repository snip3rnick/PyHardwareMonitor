from generate_stubs import buildLibreHardwareMonitor, buildPyStubbler, collectAssembly, removeExistingStubs, generateStubs
from generate_types_util import generateTypesUtilStub
from generate_namespace_init import processAllNamespaces


buildPyStubbler()
buildLibreHardwareMonitor()
collectAssembly()
removeExistingStubs()
generateStubs()
generateTypesUtilStub()
processAllNamespaces()
