# Capacity To Ship Packages Within D Days
from os import *
from sys import *
from collections import *
from math import *
def find_length_array(weights,mid):
    n=len(weights)
    sums=0
    arr=[]
    index=0
    while index<n:
        sums+=weights[index]
        if sums>mid:
            sums-=weights[index]
            arr.append(sums)
            sums=0
        else:
            index+=1
    arr.append(sums)
    l=len(arr)
    return l

def leastWeightCapacity(weights, d):
    start=max(weights)
    end =sum(weights)

    while start<=end:
        mid=(start+end)//2
        length=find_length_array(weights,mid)
        if length>d:
            start=mid+1
        else:
            end=mid-1
    return start


