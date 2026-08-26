def minmax(arr, start, end):
    if start == end:
        return (arr[start], arr[start])

    elif end == start + 1:
        if arr[start] > arr[end]:
            return (arr[end], arr[start])
        else:
            return (arr[start], arr[end])

    else:
        mid = (start + end) // 2

        min1, max1 = minmax(arr, start, mid)
        min2, max2 = minmax(arr, mid + 1, end)

        if min1 < min2:
            min_f = min1
        else:
            min_f = min2

        if max1 > max2:
            max_f = max1
        else:
            max_f = max2

        return (min_f, max_f)

arr = [10, 5, 8, 2, 15, 3, 7]

minimum, maximum = minmax(arr, 0, len(arr) - 1)

print("Array:", arr)
print("Minimum:", minimum)
print("Maximum:", maximum)