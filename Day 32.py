def NthRoot(n: int, m: int) -> int:
    # Write Your Code Here
    no=m//n
    start=0
    end=no
    while start<=end:
        mid=(start+end)//2
        power=mid**n
        if power==m:
            return mid
        elif power>m:
            end=mid-1
        else:
            start=mid+1
    return -1
