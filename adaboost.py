# DataSet: Body temperature , Gender ,Heart rate
from itertools import combinations
#import pandas as pd

def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    Point = []
    for i in f:
        List+=[i.split()]
    perm = combinations(List,2)
    for i in list(perm):
        print i
    # for x in range(len(list(perm))):
    #     #Point [list[x][0],list[x][2]]
    #     print perm
    #     # print list[x][2]
    #     print "\n"

if __name__== "__main__":
  main()
 
