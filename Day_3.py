from typing import List
global a
a=[]
def printNos(x: int) -> List[int]: 
    # Write your code here
    if x==0:
        return
    else:
        a.append(x)
        a.sort()
        printNos(x-1)
        return a

from  typing import *
def printNtimes(n: int) -> None:
    if n==0:
        return
    else:
        print("Coding Ninjas",end=" ")
        printNtimes(n-1)

from typing import List
global a
a=[]
def printNos(x: int) -> List[int]: 
    # Write your code here
    if x==0:
        return
    else:
        a.append(x)
        a.sort()
        printNos(x-1)
        return a
    
from typing import List
global a
a=[]
def printNos(x: int) -> List[int]:
    # Write your code here
    if x==0:
        return
    else:
        a.append(x)
        printNos(x-1)
        return a
    
def sumFirstN(n: int) -> int:
    # Write your code here.
    if n==0:
        return 0
    else:
        return n+sumFirstN(n-1)
    
def factorialNumbers(n):
    res=1
    cnt=1
    ans=[]
    while res <= n:
        res=res*cnt #1
        if res<=n:
            ans.append(res)
            cnt+=1
    return ans

from typing import *
def reverseArray(n: int, nums: List[int]) -> List[int]:
    # Write your code here
    for i in range(0,int(n/2)):
        if i!=(n-i-1):
            k=nums[n-i-1]
            nums[n-i-1]=nums[i]
            nums[i]=k
    return nums