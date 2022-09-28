"""
TNPG: VAT, Vivian Graeber, Ayman Habib, Talia Hsia

DISCO:
- FIles do not need an extension, the computer looks at the metadata inside the file

QCC:

OPS SUMMARY: Given a dictionary of periods with the class roster assigned to each, and a list with the period numbers, the function randomly chooses a number from the list of period numbers, stores it in the variable 'pd', and then accesses the roster for that period using the dictionary. The function then randomly selects a name from the roster and stores the name in the 'name' variable. Then, it prints out the period and the name.

"""
import random

with open("krewes.txt") as f:
    text = f.read()

devosnducky = text.split("@@@")
krewes = {2:[], 7:[], 8:[]}
for x in devosnducky:
    devoinfo = x.split("$$$")
    pd = int(devoinfo[0])
    devo = devoinfo[1]
    ducky = devoinfo[2]
    krewes[pd].append(devo + " " + ducky)

pd_list = [2, 7, 8]
pd = random.choice(pd_list)
name = random.choice(krewes[pd])
print(f"{pd} {name}")

