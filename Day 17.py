def findMissingRepeatingNumbers(a: [int]) -> [int]:
    # Write your code here
    n=len(a)
    hashes={}
    s=[]
    for i in range(n):
        if a[i] not in hashes:
            hashes[a[i]]=1
        elif a[i] in hashes:
            hashes[a[i]]+=1
    for i in range(1,n+1):
        if i in hashes and hashes[i]==2:
            s.append(i)
    for i in range(1,n+1):
        if i not in hashes:
            s.append(i)
    return s