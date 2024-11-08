from generate_stubs import collectAssembly, removeExistingStubs, generateStubs
from generate_types_util import generateTypesUtilStub
from generate_namespace_init import processAllNamespaces


collectAssembly()
removeExistingStubs()
generateStubs()
generateTypesUtilStub()
processAllNamespaces()
