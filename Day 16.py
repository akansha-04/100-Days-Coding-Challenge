# Majority Element
import math
def majorityElement(v: [int]) -> [int]:

    # Write your code here
    diction={}
    arr=[]
    n=len(v)
    for i in range(n):
        if v[i] not in diction:
            diction[v[i]]=1
        else:
            diction[v[i]]+=1
    
    for key in diction:
        if diction[key]>math.floor(n/3):
            arr.append(key)
    arr.sort()
    return arr
# Three Sum
# Bruteforce Sol
def triplet(n: int, arr: [int]) -> [[int]]:
    # Write your code here.
    s=set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if arr[i]+arr[j]+arr[k]==0:
                    temp=[arr[i],arr[j],arr[k]]
                    temp.sort()
                    s.add(tuple(temp))
    s = [list(triplet) for triplet in s]
    s=list(s)

    return s
# Better Sol
def triplet(n: int, arr: [int]) -> [[int]]:
    # Write your code here.
    s=set()
    for i in range(n):
        hashset=set()
        for j in range(i+1,n):
            k=-(arr[i]+arr[j])
            if k in hashset:
                temp=[arr[i],arr[j],k]
                temp.sort()
                s.add(tuple(temp))
            hashset.add(arr[j])
    s = [list(triplet) for triplet in s]
    s=list(s)

    return s