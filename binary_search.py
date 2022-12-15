# binary search direct approach

def binary_searchiter(arr, n):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < n:
            low = mid + 1
        elif arr[mid] > n:
            high = mid - 1
        else: 
            return mid
    return -1



# binary search with recusion

def binary_search(arr, low, high, number):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == number:
           return mid
        elif arr[mid] > number:
           return binary_search(arr, low, mid-1, number)
        else:
           return binary_search(arr, mid+1, high, number)
    else:
        return -1


# binary search with library

from  bisect import bisect_left

def Binary_Search(a, n):
    i = bisect_left(a, n)
    if i != len(a) and a[i] == n:
        return i
    else:
        return -1
