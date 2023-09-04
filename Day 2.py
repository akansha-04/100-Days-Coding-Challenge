# Problem 1
from typing import List
import math
def printDivisors(n: int) -> List[int]:
    # Write your code here
    a=[]
    for i in range(1,int(math.sqrt(n))+1):
        if n%i==0:
            a.append(i)
            if n//i!=i:
                a.append(n//i)
    a.sort()
    return a
# Problem 2
import math
## Read input as specified in the question.
## Print output as specified in the question.
n=int(input())
a=[]
for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        a.append(i)
        if n//i!=i:
            a.append(n//i)
if len(a)==2:
    print("true")
else:
    print("false")

# Problem 3
class Solution:
    def printTriangle(self, N):
        space = 2*(N-1)
        for i in range(N):
            for j in range(i+1):
                print(j+1,end=' ')
            for l in range(space):
                print(" ",end=' ')
            for k in range(i+1,0,-1):
                print(k,end=' ')
            space -= 2
            print()

# Problem 4
class Solution:
    def printTriangle(self, N):
        space = 2*(N-1)
        for i in range(N):
            for j in range(i+1):
                print(j+1,end=' ')
            for l in range(space):
                print(" ",end=' ')
            for k in range(i+1,0,-1):
                print(k,end=' ')
            space -= 2
            print()