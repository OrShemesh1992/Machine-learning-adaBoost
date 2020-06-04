
# A Python program to print all
# permutations using library function
from itertools import permutations
from itertools import combinations
# Get all permutations of [1, 2, 3]
a = [[1,2,2],[3,3,4],[5,4,6]]
f = open("HC_Body_Temperature", "r")
List = []
for i in f:
    List+=[i.split()]
perm = combinations(a,2)

# Print the obtained permutations
for i in list(perm):
    print i
