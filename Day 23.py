# Implement Lower Bound
def lowerBound(arr: [int], n: int, x: int) -> int:
    l=0
    h=n-1

    while l<=h:
        mid=(l+h)//2
        if mid!=n-1:
            if arr[mid]<x:
                l=mid+1
            if l==h and h==mid and l==mid:
                return mid
            if arr[mid]>=x:
                h=mid
        else:
            return n
        
#Implement Upper Bound
def upperBound(arr: [int], x: int, n: int) -> int:
    l=0
    h=n-1

    while l<=h:
        mid=(l+h)//2
        if arr[mid]<=x and mid!=n-1:
            l=mid+1
        if l==h and h==mid and l==mid and arr[mid]>x:
            return mid
        if l==h and h==mid and l==mid and arr[mid]<=x:
            return n
        if arr[mid]>x:
            h=mid
        


