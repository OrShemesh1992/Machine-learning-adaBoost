# DataSet: Body temperature , Gender ,Heart rate
from itertools import combinations
import random
#import pandas as pd

def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    Point = []
    for i in f:
        List+=[i.split()]
    #numberList = [111,222,333,444,555]
    List_random=random.sample(List,130)
    traning=[]
    testing=[]
    for i in range(0,65):
        traning+=[List_random[i]]
    for i in range(65,130):
        testing+=[List_random[i]]
    for i in range(len(traning)):
        print traning[i]
    # random.sample(List,2)
    # for i in range(len(List_random)):
    #     print List_random[i]
    #     print "\n"
    #print("random item from list is: ", random.choice(List))
    # perm = combinations(List,2)
    # for i in list(perm):
    #     print i
    # for x in range(len(list(perm))):
    #     #Point [list[x][0],list[x][2]]
    #     print perm
    #     # print list[x][2]
    #     print "\n"

if __name__== "__main__":
  main()
 
