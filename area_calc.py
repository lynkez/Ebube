#program that computes the area of a parcel given the coordinates or using
#the cross coordinate method

import math
import time
import sys

def strt():
    n=float(input("Enter the number of points enclosing the area: "))
    d_area=0
    count=0
    
    while count!=n:
        x = float(input("Enter first x coordinate: "))
        f = float(input("Enter y coordinate of the forward station: "))
        b = float(input("Enter y coordinate of the back station: "))
        d_area = d_area + (x*(f-b))
        count+=1
    else:
        count==n
        area = (d_area/2) *(-1)
        Area = str(area)
        print 'Area in Sqm:', Area+'Sqm'


strt()
time.sleep(10)
sys.exit
