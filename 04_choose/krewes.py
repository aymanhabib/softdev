"""
TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia

DISCO:

QCC:

OPS SUMMARY:

"""
import random
krewes = {2: ['agershkovich', 'ahabib', 'apiatetsky', 'atalukder', 'awong', 'bchen', 'cchen', '], 7:['a', 'b', 'c', 'd', 'e'], 8:['8a', '8b', '8c', '8d', '8e']}
pd_list = [2, 7, 8]
pd = random.choice(pd_list)

name = random.choice(krewes[pd])

print(str(pd) + ' ' + name)
