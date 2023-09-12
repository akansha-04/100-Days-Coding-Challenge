# Maximum Subarray Sum
from os import *
from sys import *
from collections import *
from math import *
from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)
def maxSubarraySum(arr, n) :
    sums=0
    maximum=arr[0]
    for i in range(n):
        sums+=arr[i]
        maximum=max(maximum,sums)
        if sums<0:
            sums=0
    if maximum>0:
        return maximum
    else:
        return 0
    
# Longest Subarray With Sum K
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    # Write your code here
    hashs={}
    sums=0
    length=0
    for i in range(len(a)):
        sums+=a[i]
        if sums not in hashs:
            hashs[sums]=i
        if sums==k:
            length=max(length,hashs.get(k)+1)
        if sums-k in hashs:
            temp_len=i-hashs.get(sums-k)
            length=max(length,temp_len)
    return length

# Best time to buy and sell stock
def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    minimum=prices[0]
    profit=0
    for i in range(len(prices)):
        cost=prices[i]-minimum
        profit=max(cost,profit)
        minimum=min(minimum,prices[i])
    return profit


