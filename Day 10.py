# Alternate Numbers
from typing import *
def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    b=[]
    pos=0
    neg=1
    for i in range(len(a)):
        if a[i]>0:
            b.insert(pos,a[i])
            pos+=2
        else:
            b.insert(neg,a[i])
            neg+=2
    return b

# Next Greater Permutation
from typing import *
def nextGreaterPermutation(A : List[int]) -> List[int]:
    # Write your code here.
    n=len(A)
    ind=-1
    i=n-2
    while i>=0 :
        if A[i]<A[i+1]:
            ind=i
            break
        i-=1
    if ind==-1:
        A.reverse()
        return A
    for i in range(n-1,ind,-1):
        if A[ind]<A[i]:
            A[ind],A[i]=A[i],A[ind]
            break
    A[ind+1:]=A[ind+1:][::-1]
    return A

# Superior Elements
from typing import *
def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    maximum=a[-1]
    l=len(a)
    arr=[]
    arr.append(maximum)
    for i in range(l-1,0,-1):
        if a[i-1]>maximum:
            maximum=a[i-1]
            arr.append(maximum)
    return arr


