import math


def find_max(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high) // 2
    left = find_max(arr, low, mid)
    right = find_max(arr, mid + 1, high)
    return max(left, right)
arr = [12, 45, 7, 89, 23, 56]
print(find_max(arr, 0, len(arr)-1))
