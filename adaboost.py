# DataSet: Body temperature , Gender ,Heart rate
from itertools import combinations
import random
#import pandas as pd
def FindPoint(x1, y1, x2,
              y2, x, y) :
    if (x >= x1 and x <= x2 and
        y >= y1 and y <= y2) :
        return True
    else :
        return False
def rectangle(point65) :
    perm = combinations(point65,2)
    List= list(perm)
    mini = float('inf')
    rectangle=[]
    count1=float('inf')
    count2=float('inf')
    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])
        mini=min(mini,min(count1,count2))
        rectangle=x1, y1, x2, y2
        print (i,rectangle,count1,count2,mini)
        count1=0
        count2=0
        for  j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPoint(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count1+=1
            elif not FindPoint(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count1+=1
        for  j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPoint(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count2+=1
            elif not FindPoint(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count2+=1
def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    for i in f:
        List+=[i.split()]
    List_random=random.sample(List,130)
    traning=[]
    testing=[]
    for i in range(0,65):
        traning+=[List_random[i]]
    for i in range(65,130):
        testing+=[List_random[i]]
    rectangle(traning)
if __name__== "__main__":
  main()
 
