class Solution:
    def printSquare(self, N):
        for i in range(N):
            for j in range(N):
                print("*",end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        for i in range(1,N+1):
            k=i
            for j in range(k,2*k):
                print(k,end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            for j in range(i,0,-1):
                print("*",end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N,0,-1):
            for j in range(N,N-i,-1):
                print(N-j+1,end=" ")
            print()

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            no=2*i+1
            space=N-i-1
            print(" "*space+"*"*no)


class Solution:
    def printTriangle(self, N):
        for i in range(N,0,-1):
            no=2*i-1
            space=N-i
            print(" "*space+"*"*no)

class Solution:
    def printDiamond(self, N):
        # Code here
        for i in range(N):
            no=i+1
            space=N-i-1
            print(" "*space+"* "*no)
        for i in range(N,0,-1):
            no=i
            space=N-i
            print(" "*space+"* "*no)

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            no=i+1
            print("* "*no)
        for i in range(N-1,0,-1):
            no=i
            print("* "*no)

