"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Dev Patel
ID:      212325400
Email:   pate5400@mylaurier.ca
__updated__ = "2022-03-12"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from functions import stack_reverse
# Constants
source = Stack()
source.push("element1")
source.push("element2")
source.push(3)
source.push(4)
print("The original stack is ")
for s in source:
    print(s)
stack_reverse(source)
print("The reversed stack is")
for i in source:
    print(i)
