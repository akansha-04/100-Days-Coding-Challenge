# Longest Succesive Element
# 1. bruteforce sol
from typing import *
def longestSuccessiveElements(a : List[int]) -> int:
    maximum=0
    for i in range(len(a)):
        cnt=1
        x=a[i]
        no=x+1
        while no in a:
            cnt+=1
            no+=1
        maximum=max(maximum,cnt)
    return maximum

#2.  Optimal Sol
from typing import *
def longestSuccessiveElements(a : List[int]) -> int:
    n = len(a)
    if n == 0:
        return 0

    longest = 1
    st = set(a)

    # Find the longest sequence
    for it in st:
        # if 'it' is a starting number
        if it - 1 not in st:
            # find consecutive numbers
            cnt = 1
            x = it
            while x + 1 in st:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

# Zero Matrix
# Bruteforce sol
def mark_row(matrix,row,j):
    for i in range(j):
        if matrix[row][i]!=0:
            matrix[row][i]=-1

def mark_col(matrix,col,i):
    for k in range(i):
        if matrix[k][col]!=0:
            matrix[k][col]=-1

def zeroMatrix(matrix, n, m):
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                mark_row(matrix,i,m)
                mark_col(matrix,j,n)
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==-1:
                matrix[i][j]=0 
    return matrix

# Optimal sol
from os import *
from sys import *
from collections import *
from math import *


def zeroMatrix(matrix, n, m):
    col=[]
    row=[]
    for i in range(n):
        row.append(0)
    for i in range(m):
        col.append(0)
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==0:
                row[i]=1
                col[j]=1
    for i in range(n):
        for j in range(m):
            if row[i]==1 or col[j]==1:
                matrix[i][j]=0
    return matrix
