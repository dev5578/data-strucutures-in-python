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
from morse import ByLetter
# Constants
l1 = ByLetter('K', '-.-')
l2 = ByLetter('L', '.-..')
check = l1 < l2
print(check)
