#importing importlib.util module

import importlib.util
import networkx as nx
#importing the system module
import sys
nx.DiGraph() 
# For illustration
name = 'networkx'
 
#code to check if the library exists
if (spec := importlib.util.find_spec(name)) is not None:
    #displaying that the module is found
    print(f"{name!r} already in sys.modules")
    #importing the present module
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    #displaying that the module has been imported
    print(f"{name!r} has been imported")
#else displaying that the module is absent
else:
    print(f"can't find the {name!r} module")