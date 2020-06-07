# DataSet: Body temperature , Gender ,Heart rate
from itertools import combinations
import math
from math import exp
import random
import numpy as np
def FindPointrect(x1, y1, x2,
              y2, x, y) :
    if (x >= x1 and x <= x2 and
        y >= y1 and y <= y2) :
        return True
    else :
        return False

def FindPointCircle(circle_x, circle_y, rad, x, y):

	# Compare radius of circle
	# with distance of its center
	# from given point
	if ((x - circle_x) * (x - circle_x) +
		(y - circle_y) * (y - circle_y) <= rad * rad):
		return True;
	else:
		return False;

def circle(point65,weight) :
    List= list(combinations(point65,2))
    circle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')

    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])
        rad = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if mini>min(count1,count2):
            mini=min(count1,count2)
            circle=x1, y1, x2, y2
        #print (i,circle,count1,count2,mini)
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count1+=weight[j]
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count1+=weight[j]
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count2+=weight[j]
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count2+=weight[j]
    print ("min circle:",circle,mini)
    return circle,float(mini);

def rectangle(point65,weight) :
    List= list(combinations(point65,2))
    rectangle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')
    Gender=0
    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])

        # if count1<count2 :
        #     gender = 1
        # else
        #     gender = 2
        if mini>min(count1,count2):
            mini=min(count1,count2)
            rectangle=x1, y1, x2, y2
        #print (i,rectangle,count1,count2,mini)
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count1+=weight[j]
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count1+=weight[j]
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count2+=weight[j]
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count2+=weight[j]
    print ("min rectangle:",rectangle,mini)
    return rectangle,float(mini);

def split_list(a_list):
    half=len(a_list)/2
    return a_list[:half],a_list[half:]


def adaboost(List) :
    training=[]
    testing=[]
    length=len(List)/2
    for r in range(8):
        training,testing = split_list(random.sample(List,len(List)))
        for i in range(100):
            #adaboost
            weights=[1/float(len(List))]*length
            for j in range(r):
                #minimum weighted error
                Ht = rectangle(training,weights)
                #alpha
                Alpha = float(0.5*np.log((1-Ht[1])/Ht[1]))
                print Alpha
                # update_weights
                weights=update_weights(Alpha,training,Ht[0],weights)
                #normalizion
                weights=normalize_weight(weights)

def update_weights(alpha, training,rec, weights):
    for z in range(len(training)):
        if FindPointrect(rec[0],rec[1],rec[2],rec[3],training[z][0],training[z][2]):
            weights[z] = weights[z] * exp(alpha)
            print("alpha",weights[z])
        else:
            weights[z] = weights[z] * exp(-alpha)
            print("-alpha",weights[z])
    return weights;

def normalize_weight(weights):
    sum_of_weights =sum(weights)
    for z in range(len(weights)):
        weights[z] = weights[z] / sum_of_weights
    return weights;

def main():
    f = open("HC_Body_Temperature", "r")
    List = []
    for i in f:
        List+=[i.split()]
    adaboost(List)
if __name__== "__main__":
  main()
 
