"""
TNPG: Pink Oranges, Ryan Lau, Ayman Habib

DISCO:

QCC:

OPS:

"""

"""
import csv
import random
occu = {}
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        occu[row[0]] = float(row[1])
var = random.choices(list(occu.keys()), list(occu.values()))
print(var)
"""
import random 

with open('occupations.csv') as f:
    text = f.read()
 
lines = text.split('\n')
occudict = {}
for x in lines[1:-1]:
    pieces = x.split(',')
    occudict[",".join(pieces[0:-1])] = float(pieces[-1])

nums = []
for key in list(occudict.keys()):
    count = int(occudict[key] * 10)
    for i in range(count):
        nums.append(key)
    
print(random.choice(nums))