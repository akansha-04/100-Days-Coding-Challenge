# Two Sum
    l,r=0,n-1
    s=sorted(book)
    while l<r:
        sum=s[l]+s[r]
        if sum==target:
            return "YES"
        if s[l]+s[r]<target:
            l+=1
        else:
            r-=1

    return "NO"
'''
for i in range(n):
        chk=target-book[i]
        if chk in book:
            return "YES"
            break
    return "NO"
'''

# Sort An Array of 0s, 1s and 2s
from os import *
from sys import *
from collections import *
from math import *
def sortArray(arr, n):

	# Write your code here
	c_0=c_1=c_2=0
	for i in arr:
		if i==0:
			c_0+=1
		elif i==1:
			c_1+=1
		else:
			c_2+=1
	arr[0:c_0]=[0]*c_0
	arr[c_0:c_0+c_1]=[1]*c_1
	arr[c_0+c_1:c_0+c_1+c_2]=[2]*c_2
	return arr
# Majority Element
def majorityElement(v: [int]) -> int:
    # Write your code here
    dicts={}
    for i in range(len(v)):
        if v[i] not in dicts:
            dicts[v[i]]=1
        else:
            dicts[v[i]]+=1
    for i in dicts:
        if dicts[i]>=int(len(v)/2):
            return i
            break 
# Rotate array

from os import *
from sys import *
from collections import *
from math import *
# n-i-k
#Your code goes here.

n=int(input())
arr=list(input().split(" "))
k=int(input())
temp=[]
temp=arr[:k]

for i in range(k,n):
    arr[i-k]=arr[i]
arr[n-k:n]=temp
print(" ".join(arr))