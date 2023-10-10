# Square root using binary search
def floorSqrt(n):
   start=0
   end=n
   while start<=end:
      mid=(start+end)//2
      square=mid*mid
      if square==n:
         return mid

      elif square<n:
         start=mid+1
         a=mid
      else:
         end=mid-1
         
   return a
         
      
   
n= int(input())
print(floorSqrt(n))