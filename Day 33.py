# Rose garden
from typing import List
def possible(arr, day, m, r):
    n = len(arr)  # size of the array
    cnt = 0
    noOfB = 0
    # count the number of bouquets
    for i in range(n):
        if arr[i] <= day:
            cnt += 1
        else:
            noOfB += cnt // r
            cnt = 0
    noOfB += cnt // r
    return noOfB >= m



def roseGarden(arr: List[int], r: int, b: int):
    val = b * r
    n = len(arr)  # size of the array
    if val > n:
        return -1  # impossible case
    # find maximum and minimum
    mini = float('inf')
    maxi = float('-inf')
    for i in range(n):
        mini = min(mini, arr[i])
        maxi = max(maxi, arr[i])

    # apply binary search
    low = mini
    high = maxi
    while low <= high:
        mid = (low + high) // 2
        if possible(arr, mid, b, r):
            high = mid - 1
        else:
            low = mid + 1
    return low