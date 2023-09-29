# Search Insert Position
def searchInsert(arr: [int], m: int) -> int:
    # Write your code here.
    n=len(arr)
    l=0
    h=n-1
    ans=-1
    while l<=h:
        mid=(l+h)//2
        if arr[mid]<m:
            ans=mid
            l=mid+1
        elif arr[mid]>m:
            h=mid-1
        elif arr[mid]==m:
            ans=mid-1
            l=mid+1
    return ans+1        

from os import *
from sys import *
from collections import *
from math import *

# Floor and Ceil in Sorted Array
def ceilingInSortedArray(n, x, arr):
    arr.sort()
    l=0
    n=len(arr)
    h=n-1
    ans=-1
    sec_ans=arr[0]
    while l<=h:
        mid=(l+h)//2
        if arr[mid]<x:
            if mid!=n-1:
                ans=arr[mid]
                sec_ans=arr[mid+1]
            elif mid==n-1:
                ans=arr[mid]
                sec_ans=-1
            l=mid+1
        elif arr[mid]>x:
            h=mid-1
        elif arr[mid]==x:
            ans=arr[mid]
            sec_ans=arr[mid]
            l=mid+1
    c=str(ans)+" "+str(sec_ans)
    return c

# First and Last Position of an Element In Sorted Array
def binary_first(arr, n, k):
    s, e, pos = 0, n - 1, -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == k:
            pos = mid
            e = mid - 1
        elif arr[mid] < k:
            s = mid + 1
        else:
            e = mid - 1
    return pos

def binary_last(arr, n, k):
    s, e, pos = 0, n - 1, -1
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == k:
            pos = mid
            s = mid + 1
        elif arr[mid] < k:
            s = mid + 1
        else:
            e = mid - 1
    return pos

def firstAndLastPosition(arr, n, k):
    first_pos = binary_first(arr, n, k)
    last_pos = binary_last(arr, n, k)
    return (first_pos, last_pos)
