# Merge Two Sorted Arrays Without Extra Space
from typing import *

def mergeTwoSortedArraysWithoutExtraSpace(a : List[int], b : List[int]) -> int:
    # Write your code here.
    n=len(a)
    m=len(b)
    left = n - 1
    right = 0

    # Swap the elements until a[left] is smaller than b[right]:
    while left >= 0 and right < m:
        if a[left] > b[right]:
            a[left], b[right] = b[right], a[left]
            left -= 1
            right += 1
        else:
            break

    # Sort a[] and b[] individually:
    a.sort()
    b.sort()