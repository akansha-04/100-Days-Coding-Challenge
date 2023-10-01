def firstOccurrence(arr, n, k):
    low = 0
    high = n - 1
    first = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            first = mid
            # look for smaller index on the left
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return first


def lastOccurrence(arr, n, k):
    low = 0
    high = n - 1
    last = -1

    while low <= high:
        mid = (low + high) // 2
        # maybe an answer
        if arr[mid] == k:
            last = mid
            # look for larger index on the right
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1  # look on the right
        else:
            high = mid - 1  # look on the left

    return last

def firstAndLastPosition(arr, n, k):
    first = firstOccurrence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = lastOccurrence(arr, n, k)
    return (first, last)


def count(arr: [int], n: int, x: int) -> int:
    # Your code goes here
    first, last = firstAndLastPosition(arr, n, x)
    if first == -1:
        return 0
    return last - first + 1


            
