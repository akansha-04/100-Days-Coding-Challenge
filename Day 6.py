# Move zeroes to end
def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    c=a.count(0)

    for i in range(c):
        a.remove(0)
        a.append(0)
    return a

# Linear Search
def linearSearch(n: int, num: int, arr: [int]) -> int:
    # Write your code here.
    if num in arr:
        return arr.index(num)
    return -1

# Find the Union
def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    c=[]
    for i in range(len(a)):
        if a[i] not in c:
            c.append(a[i])
    for j in range(len(b)):
        if b[j] not in c:
            c.append(b[j])
    c.sort()
    return c

# Find the Single element
from typing import *
def getSingleElement(arr : List[int]) -> int:
    # Write your code here.
    n=len(arr)
    ans = 0
    for i in range(1,n,2):
        if(arr[i-1] != arr[i]):
            ans = arr[i-1]
            return ans
    return arr[n-1]