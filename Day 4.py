# Selection sort
from typing import List
def selectionSort(arr: List[int]) -> None: 
    # Write your code here
    for i in range(len(arr)):
        if i!=len(arr)-1:
            new_arr=arr[i:len(arr)]
            minimum=min(new_arr)
        else:
            minimum=arr[len(arr)-1]
            break
        index_min=new_arr.index(minimum)+i
        subs=arr[i]
        arr[i]=minimum
        arr[index_min]=subs
    return arr

# Bubble sort
from typing import List
def bubbleSort(arr: List[int], n: int):
    # Your code goes here.
    for i in range(n,0,-1):
        for j in range(0,i):
            if j!=n-1:
                if arr[j]>arr[j+1]:
                    temp=arr[j+1]
                    arr[j+1]=arr[j]
                    arr[j]=temp
    return arr

# Insertion Sort
from typing import List
def insertionSort(a: List[int], n: int) -> None:
   # write your code here
      for i in range(0,n):
         if i!=n-1:
            for j in range(i+1,0,-1):
               if a[j]<a[j-1] and j>0:
                  temp=a[j]
                  a[j]=a[j-1]
                  a[j-1]=temp
      return a

# Largest Element in array
from sys import *
from collections import *
from math import *
def largestElement(arr: [], n: int) -> int:
    maximum=max(arr)
    return maximum

# Second Largest Number
def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    a.sort()
    arr=[]
    arr.append(a[-2])
    arr.append(a[1])
    return arr

# Check if array is sorted
def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    b=a[:]
    b.sort()
    if a==b:
        return 1
    else:
        return 0
    
# remove duplicates from sorted array
def removeDuplicates(arr,n):
    # Write your code here.
    a=[]
    for i in arr:
        if i not in a:
            a.append(i)
    l=len(a)
    return l
