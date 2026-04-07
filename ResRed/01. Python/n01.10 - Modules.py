# Module = a file containing code you want to include in your program
#          use 'import' to include a module (built-in or your own)
#          useful to break up a large program reusable separate files

# print(help("modules")) # list all modules
# print(help("math")) # module for module - lol

import math # to import module
#or
import math as m

print(math.pi) # to prove a module
print(m.pi)

# for specific
from math import pi # not recommended tho, can conflict with variables
print(pi)

import createmodule as module

print(module.pi)
print(module.square(3))
print(module.cube(3))
print(module.circumference(15))
print(module.area(23))