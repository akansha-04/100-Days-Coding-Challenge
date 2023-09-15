# Rotate The Matrix
from typing import *
def rotateMatrix(mat : List[List[int]]):
    n = len(mat)
    for i in range(n):
        for j in range(i, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    for i in range(n):
        mat[i] = mat[i][::-1]


     