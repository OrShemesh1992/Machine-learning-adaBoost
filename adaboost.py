# DataSet: Body temperature , Gender ,Heart rate
from __future__ import print_function
from itertools import combinations
import math
from math import exp
import random
import numpy as np

# ************ Find Point rectangle *************
# Check if the point is inside the rectangle
def FindPointrect(x1, y1, x2,
              y2, x, y) :
    if (x >= x1 and x <= x2 and
        y >= y1 and y <= y2) :
        return True
    else :
        return False

# ************ Find Point Circle *************
# Check if the point is inside the circle
# Compare radius of circle with distance of its cente from given point
def FindPointCircle(circle_x, circle_y, rad, x, y):
	if ((x - circle_x) * (x - circle_x) +
		(y - circle_y) * (y - circle_y) <= rad * rad):
		return True;
	else:
		return False;

# ************ circle *************
# This function get 65 points, Prepares all combinations for circles and
# checks whether the points inside are with a certain gender and the outside with another gender.
# If the gender is different from what is defined it is called a mistake
def circle(point65,weight) :
    List= list(combinations(point65,2))
    circle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')
    Gender=0
    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])
        rad = math.sqrt((x1-x2)**2+(y1-y2)**2)
        if mini>min(count1,count2):
            mini=min(count1,count2)
            circle=x1, y1, x2, y2
            if  count1<count2:
                Gender = 1
            else :
                Gender =-1
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count1+=weight[j]
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count1+=weight[j]
            if FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==1:
                count2+=weight[j]
            elif not FindPointCircle(x1, y1, rad, x, y) and float(point65[j][1])==2:
                count2+=weight[j]
    return circle,float(mini),Gender;

# ************ rectangle *************
# This function get 65 points, Prepares all combinations for rectangles and
# checks whether the points inside are with a certain gender and the outside with another gender.
# If the gender is different from what is defined it is called a mistake
def rectangle(point65,weight) :
    List= list(combinations(point65,2))
    rectangle=[]
    mini,count1,count2 = float('inf'),float('inf'),float('inf')
    Gender=0
    for i in range(len(List)):
        x1 , y1 , x2 , y2 = float(List[i][0][0]),float(List[i][0][2]),float(List[i][1][0]),float(List[i][1][2])
        if mini>min(count1,count2):
            mini=min(count1,count2)
            rectangle=x1, y1, x2, y2
            if count1<count2:
                Gender = 1
            else :
                Gender =-1
        count1=0
        count2=0
        for j in range(len(point65)):
            x , y=float(point65[j][0]),float(point65[j][2])
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count1+=weight[j]
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count1+=weight[j]
            if FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==1:
                count2+=weight[j]
            elif not FindPointrect(x1, y1, x2, y2, x, y) and float(point65[j][1])==2:
                count2+=weight[j]
    return rectangle,float(mini),Gender;

# ************ function helper split list *************
# The function splits the list to 2 in the middle
def split_list(a_list):
    half=len(a_list)/2
    return a_list[:half],a_list[half:]

#******************adaboost******************
#The output of the other learning algorithms ('weak learners')
#is combined into a weighted sum that represents the final output of the boosted classifier
def adaboost(List,rec_cir) :
    training=[]
    testing=[]
    Setofrules=[]
    length=len(List)/2
    AvgTest,AvgTrain=0,0;
    for r in range(1,9):
        AvgTest=0
        AvgTrain=0
        for i in range(100):
            training,testing = split_list(random.sample(List,len(List)))
            AvgTest+=test(Setofrules,testing,rec_cir)
            AvgTrain+=test(Setofrules,training,rec_cir)
            Setofrules=[]
            #******************adaboost main code******************
            weights=[1/float(len(training))]*length
            for j in range(r):
                #minimum weighted error
                if float(rec_cir)==1:
                    Ht = rectangle(training,weights)
                elif float(rec_cir)==2:
                    Ht = circle(training,weights)
                #alpha
                Alpha = float(0.5*np.log((1-Ht[1])/Ht[1]))
                # update_weights
                weights=update_weights(Alpha,training,Ht[0],weights,rec_cir)
                #normalizion
                weights=normalize_weight(weights)
                #add to set
                Setofrules+=[Ht]
        print("Average testing errors in round " ,r, " :",(float(AvgTest)/100)/65,sep=" ")
        print("Average training errors in round " ,r, " :", (float(AvgTrain)/100)/65,sep=" ")

# ******************testing*******************
#Taking the points and checking their mistake on the set of rules
def test(Setofrules,testing,rec_cir):
    eror1,eror2=float('inf'),float('inf')
    Sum=0
    genderSet=0
    for j in  range(len(testing)):
        x,y =float(testing[j][0]),float(testing[j][2])
        gender =float(testing[j][1])
        Sum+=int(min(eror1,eror2)*genderSet<0)
        eror1=0
        eror2=0
        if float(rec_cir)==1:
            for i in range(len(Setofrules)):
                x1 , y1 , x2 , y2 = float(Setofrules[i][0][0]),float(Setofrules[i][0][1]),float(Setofrules[i][0][2]),float(Setofrules[i][0][3])
                alpha =Setofrules[i][1]
                genderSet=float(Setofrules[i][2])
                if FindPointrect(x1, y1, x2, y2, x, y) and gender==1:
                    eror1+=alpha
                elif FindPointrect(x1, y1, x2, y2, x, y) and gender==2:
                    eror1-=alpha
                elif not FindPointrect(x1, y1, x2, y2, x, y) and gender==1:
                    eror2+=alpha
                elif not FindPointrect(x1, y1, x2, y2, x, y) and gender==2:
                    eror2-=alpha
        elif float(rec_cir)==2:
            for i in range(len(Setofrules)):
                x1 , y1 , x2 , y2 = float(Setofrules[i][0][0]),float(Setofrules[i][0][1]),float(Setofrules[i][0][2]),float(Setofrules[i][0][3])
                rad = math.sqrt((x1-x2)**2+(y1-y2)**2)
                alpha =Setofrules[i][1]
                genderSet=float(Setofrules[i][2])
                if FindPointCircle(x1, y1, rad, x, y) and gender==1:
                    eror1+=alpha
                elif FindPointCircle(x1, y1, rad, x, y) and gender==2:
                    eror1-=alpha
                elif not FindPointCircle(x1, y1, rad, x, y) and gender==1:
                    eror2+=alpha
                elif not FindPointCircle(x1, y1, rad, x, y) and gender==2:
                    eror2-=alpha
    return Sum;


# ******************update_weights*******************
def update_weights(alpha, training,points, weights,rec_cir):
    if float(rec_cir)==1:
        for z in range(len(training)):
            if FindPointrect(float(points[0]),float(points[1]),float(points[2]),float(points[3]),float(training[z][0]),float(training[z][2])):
                weights[z] = weights[z] * exp(alpha)
            else:
                weights[z] = weights[z] * exp(-alpha)
    elif float(rec_cir)==2:
        for z in range(len(training)):
            x1 , y1 , x2 , y2 = float(points[0]),float(points[1]),float(points[2]),float(points[3])
            rad = math.sqrt((x1-x2)**2+(y1-y2)**2)
            x,y=float(training[z][0]),float(training[z][2])
            if FindPointCircle(x1, y1, rad, x, y):
                weights[z] = weights[z] * exp(alpha)
            else:
                weights[z] = weights[z] * exp(-alpha)
    return weights;

#*********************normalizion********************
def normalize_weight(weights):
    sum_of_weights =sum(weights)
    for z in range(len(weights)):
        weights[z] = weights[z] / sum_of_weights
    return weights;

#*********************Main***************************
def main():
    f = open("HC_Body_Temperature", "r") #The dataset
    List = []
    for i in f:
        List+=[i.split()]
    rec_cir = raw_input("click 1 for Rectangle or 2 for Circle : ")
    if float(rec_cir)<1 or float(rec_cir)>2:
        print("try again")
        return;
    print("wait a few minitus ... calculating")
    adaboost(List,rec_cir)
if __name__== "__main__":
  main()
