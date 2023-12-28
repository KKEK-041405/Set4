Creating a dictionary is as simple as placing items inside curly braces {} separated by

commas. An item has a key and a corresponding value that is expr

essed as a pair 

(key:

value). While the values can be of any data type and can repeat, keys must be of

immutable type 

(string

, number or tuple with immutable elements) and must be unique

.

PROGRAM:

names = {}

n = int(input('Enter number of names'))

for i in

q range(n):

 names[i+1]=input('Enter a name') name = list(names.values())

pos = int(input('Enter position'))

name.sort(key=lambda x:x[pos])

print(name)
