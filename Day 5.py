# Left Rotate an array

from os import *
from sys import *
from collections import *
from math import *

def rotateArray(arr: [], n: int) -> []:
    # Write your code from here.
    temp=arr[0]
    for i in range(1,n):
        arr[i-1]=arr[i]
    arr[n-1]=temp
    return arr

# Merge Sort

def merge(arr,l,mid,r):
    n_1 = mid - l + 1
    n_2 = r - mid

    left_array = arr[l:mid + 1]
    right_array = arr[mid + 1:r + 1]

    i = 0
    j = 0
    k = l 
    while i < n_1 and j < n_2:
        if left_array[i] <= right_array[j]:
            arr[k] = left_array[i]
            i += 1
        else:
            arr[k] = right_array[j]
            j += 1
        k += 1

    while i < n_1:
        arr[k] = left_array[i]
        i += 1
        k += 1
    while j < n_2:
        arr[k] = right_array[j]
        j += 1
        k += 1


def mergeSort(arr: [int], l: int, r: int):
    # Write Your Code Here
    if l < r:
        mid = (l + r) // 2 
        mergeSort(arr, l, mid)
        mergeSort(arr, mid + 1, r)
        merge(arr, l, mid, r)