"""
TNPG: Pink Oranges, Ryan Lau, Ayman Habib

DISCO: 
    - We learned about csv.reader which reads through the file without having to do it manually
    - We learned about random.choices, which picks an item from a list using an associated list of values to assign weights

QCC:

HOW THIS FILE WORKS: 
    - First, the program reads through the csv file, splitting the data by every new line
    - Then, a dictionary is created, and each of the lines are split by commas (','), with everything before the last number in the line serving as the key, and the number serving as the value
    - A new list is made and depending on the value of the key, the key is added to the list proportionally to the value of the key times 10
    - Then, the program randomly selects an item from that list and prints it

import csv
import random
occu = {}
with open('occupations.csv') as csvfile:
    reader = csv.reader(csvfile)
    print(reader)
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